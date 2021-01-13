import PySimpleGUI as Sg
from windows.settings_window import SettingsWindow
from windows.game_window import GameWindow
from settings import Settings
from windows import ICON_FILE, HOME_IMG_FILE

KEY_SETTINGS = '-settings-'

KEY_CLOSE = '-close-'

KEY_NEW_GAME = '-newgame-'

default_window_size = (1000, 500)


class HomeScreen:

    @staticmethod
    def home_screen():
        layout = [
            # [
            #     Sg.Image(
            #         HOME_IMG_FILE,
            #         background_color='#e3e3e3',
            #
            #     )
            # ],
            [
                Sg.Text('Welcome to Tambola House',
                        background_color='#e3e3e3',
                        text_color='black',
                        auto_size_text=True,
                        size=(0, 2),
                        justification='center',
                        font=('Helvetica', 20)
                        )
            ],
            [
                Sg.Button("New Game", size=(10, 1), font=('Helvetica', 12),
                          button_color=("white", '#9343c4'), border_width=0, key=KEY_NEW_GAME)
            ],
            [
                Sg.Button("Settings", size=(10, 1), font=('Helvetica', 12),
                          button_color=("white", '#9343c4'), border_width=0, key=KEY_SETTINGS)
            ],
            [
                Sg.Button("Close", size=(10, 1), font=('Helvetica', 12),
                          button_color=("white", '#9343c4'), border_width=0, key=KEY_CLOSE)
            ]
        ]

        window = Sg.Window(
            f'Tambola',
            layout,
            background_color='#e3e3e3',
            element_justification='center',
            text_justification='center',
            disable_close=True,
            icon=ICON_FILE,
            resizable=True
        )

        return window

    def __init__(self, settings=Settings()):
        self.window = self.home_screen()
        self.settings = settings

    def run(self):
        event = ''
        while event != KEY_CLOSE:
            event, value = self.window.read()
            if event == KEY_SETTINGS:
                self.settings = SettingsWindow(self.settings).run()
            elif event == KEY_NEW_GAME:
                self.settings = GameWindow(self.settings).run()

        self.window.close()
