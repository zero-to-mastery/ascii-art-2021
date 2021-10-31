"""
Configuration for the Flask web-app.

This is usually just called `config.py` - but this is to avoid confusion
for those unfamiliar with Flask.
"""
import os

UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'webapp/uploads')
TXT_FOLDER = os.environ.get('TXT_FOLDER', 'webapp')
ASCII_IMAGE_FOLDER = os.environ.get('ASCII_IMAGE_FOLDER', 'webapp')
MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', f"{4 * 1024 * 1024}"))  # File max size set to 4MB
KEY_FOLDER = os.environ.get('KEY_FOLDER', 'keys/akey.txt')
DEFAULT_IMAGE_PATH = os.environ.get('DEFAULT_IMAGE_PATH', 'example/ztm-logo.png')
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
