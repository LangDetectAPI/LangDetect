from __future__ import annotations

import logging
import sys
from typing import Optional, TextIO

_logger: Optional[logging.Logger] = None


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
