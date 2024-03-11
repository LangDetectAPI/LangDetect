from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Any
import time
import sys

import logging

from tf_keras.models import load_model

_logger: Optional[logging.Logger] = None

langs = {'eng': 'English', 'deu': 'German', 'fra': 'French', 'spa': 'Spanish', 'ita': 'Italian',
         'tur': 'Turkish',
         'rus': 'Russian',
         'ell': 'Greek',
         'dan': 'Danish', 'fin': 'Finnish',
         'ara': 'Arabic', 'heb': 'Hebrew', 'zho': 'Chinese', 'hin': 'Hindi', 'jpn': 'Japanese', 'fas': 'Persian',
         'kor': 'Korean',
         'lat': 'Latin',
         'nor': 'Norwegian'
         }


class LangDetect:
    def __init__(self, verbose: bool = False, debug: bool = False, ) -> None:

        self._log = get_logger("LangDetect")

        self._default_model_name = "shallow_model_v1"

        if verbose:
            self._log.setLevel(logging.INFO)

        if debug:
            self._log.setLevel(logging.DEBUG)

        self._model_dir = (
                Path(__file__).parent / "models" / self._default_model_name
        )

        if not self._model_dir.is_dir():
            raise LangDetectError(f"model dir not found at {str(self._model_dir)}")

        self._assets_dir = (
                Path(__file__).parent / "models" / "assets"
        )
        self._assets_labels_path = self._assets_dir / "labels" / "vocabulary.txt"

        if not self._assets_dir.is_dir():
            raise LangDetectError(f"assets dir not found at {str(self._assets_dir)}")
        if not self._assets_labels_path.is_file():
            raise LangDetectError(f"labels vocabulary not found at {str(self._assets_labels_path)}")

        self._session = self._init_session()

        self._target_labels_space = self._init_labels_vocabulary()

    def detect(self, text: str) -> Dict[str, str]:
        """
        Detect the language of a given text.
        Args:
            text (str): Text to detect the language from.
        Returns:
            Dict[str, str]: Language detected and its name.
        """
        if not text:
            raise LangDetectError("text is required")

        start_time = time.time()
        predictions = self._get_model_outputs([text])
        elapsed_time = time.time() - start_time
        self._log.debug(f"DL prediction done in {elapsed_time:.03f} seconds")
        lang = predictions[0][0][0]
        proba=predictions[0][0][1]
        lang_name = langs.get(lang, "Unknown")

        # print(predictions)

        return {"lang_name": lang_name, "lang": lang, "proba": proba}

    def detect_batch(self, texts: List[str]) -> List[Dict[str, str]]:
        """
        Detect the language of a list of texts.
        Args:
            texts (List[str]): List of texts to detect the language from.
        Returns:
            List[Dict[str, str]]: List of languages detected and their names.
        """
        if not texts:
            raise LangDetectError("texts are required")

        start_time = time.time()
        predictions = self._get_model_outputs(texts)
        elapsed_time = time.time() - start_time
        self._log.debug(f"DL prediction done in {elapsed_time:.03f} seconds")

        return [{"lang": pred[0][0], "proba": pred[0][1]} for pred in predictions]

    def _init_session(self) -> Any:
        start_time = time.time()
        session = load_model(self._model_dir, compile=False)

        elapsed_time = time.time() - start_time
        self._log.debug(
            f'KERAS DL model "{self._model_dir}" loaded in {elapsed_time:.03f} seconds'
        )
        return session

    def _init_labels_vocabulary(self) -> List[str]:

        start_time = time.time()

        with open(self._assets_labels_path, "r") as f:
            self._target_labels_space = f.read().splitlines()
        elapsed_time = time.time() - start_time
        self._log.debug(
            f'Labels vocab "{self._assets_labels_path}" loaded in {elapsed_time:.03f} seconds'
        )

        return self._target_labels_space

    @staticmethod
    def _char_tokenizer(input_text: str):
        """
        Tokenize un texte donné en caractères, en séparant chaque caractère par un espace,
        en gardant les signes de ponctuation collés au mot qui les précède, et en supprimant
        tous les chiffres.

        Args:
            input_text (str): Texte à tokenizer.
        Returns:
            str: Chaîne de caractères tokenizée sans les chiffres.
        """

        # Liste des ponctuations
        ponct = [',', '.', '!', '?', ':', ';', '\'', "י", '"', "(", ")", "-", "–"]

        tokenized_text = ''

        # Parcourt chaque caractère du texte d'entrée
        for i, c in enumerate(input_text):

            if c not in '0123456789\n\t':  # Exclut les chiffres et certains caractères spéciaux
                # Si le caractère actuel est de la ponctuation et n'est pas le premier du texte, retire l'espace
                # précédent
                if i > 0 and input_text[i - 1] != ' ' and c in ponct:
                    tokenized_text = tokenized_text.rstrip()  # Enlève l'espace précédent si nécessaire

                # Ajoute le caractère actuel au texte tokenizé
                tokenized_text += c

                # Ajoute un espace après le caractère s'il n'est pas de la ponctuation ou s'il est suivi d'un
                # caractère non ponctuation
                if i < len(input_text) - 1 and (c not in ponct or input_text[i + 1] not in ponct):
                    tokenized_text += ' '

        return tokenized_text

    def _get_raw_predictions(self, text_list: List[str]) -> Any:
        """
        Given a list of text, return a (labels,stats, features_size)
        matrix encoding the predictions.
        """
        start_time = time.time()
        X = []
        for text in text_list:
            X.append(self._char_tokenizer(text))

        elapsed_time = time.time() - start_time
        self._log.debug(f"DL input prepared in {elapsed_time:.03f} seconds")

        start_time = time.time()
        raw_predictions = self._session.predict(X, verbose=False)

        elapsed_time = time.time() - start_time
        self._log.debug(f"DL raw prediction in {elapsed_time:.03f} seconds")
        return raw_predictions

    def _get_model_outputs(
            self, input: List[str]
    ) -> List[Any]:
        raw_preds = self._get_raw_predictions(input)
        preds_idxs = []
        for row in raw_preds:
            preds_idxs.append([(x, float(f"{p:.03f}")) for p, x in
                               sorted(zip(row, self._target_labels_space), key=lambda pair: pair[0],
                                      reverse=True, )])

        return preds_idxs


class LangDetectError(Exception):
    pass


def get_logger(name: str = None) -> logging.Logger:
    global _logger

    if _logger is None:
        _logger = logging.getLogger(name)

        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        _logger.addHandler(handler)

    return _logger


if __name__ == "__main__":
    lang_detect = LangDetect(verbose=True, debug=True)
    result = lang_detect.detect_batch(["un text pour tester la detection de langue",
                                       "The model has as input a dict of features with different types."
                                          , "Невозможно удалить цвет фона диаграммы после установки"
                                          ,
                                       "El modelo tiene como entrada un diccionario de características con diferentes tipos."
                                          , "پس از تنظیم نمی توان رنگ پس زمینه نمودار را حذف کرد"
                                          , "Grafiğin arka plan rengi ayarlandıktan sonra kaldırılamıyor",
                                       "لا يمكن إزالة لون خلفية المخطط بمجرد تعيينه"])

    print(f"Language detected: {result}")

    result = lang_detect.detect("un text pour tester la detection de langue")

    print(f"Language detected: {result}")
