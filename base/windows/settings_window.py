import PySimpleGUI as Sg
from settings import Settings

READ_SPEED_FAST = '-fast-'

SOUND_KEY = '-sound-'
READ_KEY = '-read-'
READ_SLOW_KEY = '-read_slow-'
DONE_KEY = '-done-'


class SettingsWindow:

    def get_setting_windows(self):
        layout = [
            [
                Sg.Frame(
                    "Settings",
                    [
                        [
                            Sg.Checkbox('Sound', default=self.setting.sound, enable_events=True, key=SOUND_KEY,
                                        background_color='#9343c4')
                        ],
                        [
                            Sg.Checkbox('Read', default=self.setting.read, enable_events=True, key=READ_KEY,
                                        background_color='#9343c4')
                        ],
                        [
                            Sg.Text('Read Speed',  background_color='#9343c4'),
                            Sg.Radio('Slow', '1', key=READ_SLOW_KEY, background_color='#9343c4',
                                     default=self.setting.read_slow),
                            Sg.Radio('Fast', '1', key=READ_SPEED_FAST, background_color='#9343c4',
                                     default=not self.setting.read_slow)
                        ]
                    ],

                    size=(300, 0),
                    background_color='#9343c4'
                ),
            ],
            [
                Sg.Button('Done', key=DONE_KEY, button_color=('#9343c4', 'white'), border_width=0)
            ]
        ]

        return Sg.Window('Settings', layout, disable_close=True, element_justification='center',
                         background_color='#9343c4', button_color=('white', '#9343c4'))

    def __init__(self, setin=Settings()):
        self.setting = setin
        self.window = self.get_setting_windows()

    def run(self):
        event = ''
        while event != DONE_KEY:
            event, value = self.window.read()
            self.setting.sound = value[SOUND_KEY]
            self.setting.read = value[READ_KEY]
            self.setting.read_slow = value[READ_SLOW_KEY]
            self.window[READ_SLOW_KEY].update(disabled=not self.setting.read)
            self.window[READ_SPEED_FAST].update(disabled=not self.setting.read)

        self.window.close()
        return self.setting
