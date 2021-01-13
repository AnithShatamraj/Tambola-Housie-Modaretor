import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")

    return os.path.join(base_path, relative_path)


DATA_DIR = resource_path('data')
AUDIO_DIR = os.path.join(DATA_DIR, 'audio')
IMAGES_DIR = os.path.join(DATA_DIR, 'images')
SLOW_VOICE_DIR = os.path.join(AUDIO_DIR, 'numbers-slow')
FAST_VOICE_DIR = os.path.join(AUDIO_DIR, 'numbers-fast')
BELL_SOUND_FILE = os.path.join(AUDIO_DIR, 'bell.mp3')
ICON_FILE = os.path.join(IMAGES_DIR, 'tambola-ico.ico')
HOME_IMG_FILE = os.path.join(IMAGES_DIR, 'Tambola.png')

