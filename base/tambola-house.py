from windows.home_screen import HomeScreen
from windows import AUDIO_DIR, SLOW_VOICE_DIR, FAST_VOICE_DIR, BELL_SOUND_FILE

if __name__ == '__main__':
    print('AUDIO_DIR', AUDIO_DIR)
    print('SLOW_VOICE_DIR', SLOW_VOICE_DIR)
    print('FAST_VOICE_DIR', FAST_VOICE_DIR)
    print('BELL_SOUND_FILE', BELL_SOUND_FILE)
    HomeScreen().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

