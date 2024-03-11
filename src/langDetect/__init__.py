import dotenv

from .langDetect import LangDetect
from .logger import get_logger

LangDetector = LangDetect.LangDetector
LangDetectorError = LangDetector.LangDetectorError

get_logger = get_logger

__all__ = ["LangDetector", "LangDetectorError", "get_logger"]

dotenv.load_dotenv(dotenv.find_dotenv())
