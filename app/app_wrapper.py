import os
import sys
from loguru import logger


logger.remove()
logger.add(
    sys.stderr,
    format='{level} | {module} | {function} | {message}',
    level=os.getenv('LOG_LEVEL', 'INFO').upper()
)

from app.main import app
