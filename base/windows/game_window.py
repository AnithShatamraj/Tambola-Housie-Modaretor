import PySimpleGUI as Sg
from windows.settings_window import SettingsWindow
from windows.end_game_prompt import EndGamePrompt
from windows.view_order import ViewOrder
from windows.validate_ticket import ValidateTicket
from windows import FAST_VOICE_DIR, SLOW_VOICE_DIR, BELL_SOUND_FILE
from game import Game
from pygame import mixer
from helpers.layout_helpers import table_of_numbers
import random
import time

KEY_REMAINING = '-remaining-'

KEY_COMPLETED = '-completed-'

KEY_VIEW_ORDER = '-viewhist-'

KEY_VAL_TICKET = '-valticket-'

KEY_POP_HEAD = '-pophead-'

KEY_POP = '-POP-'

KEY_HIST_HEAD = '-histhead-'

KEY_HIST = '-HIST-'

KEY_NEXTNUM = '-nxtnum-'

KEY_AUTO_PLAY = '-autoplay-'

KEY_ENDGAME = '-endgame-'

KEY_SETTINGS = '-settings-'

default_window_size = (1000, 500)

luck_liners = [
    'Any luck? May be next time',
    'Yeeesss! Not your number :( ?',
    'Missed it by 1!!!!',
    'How is that?... good enough?',
    'Finally...!',
    'Come on, no one yet',
    'The wait is over....?'
]

colors = [
    '#005aeb',
    '#00bedb',
    '#fa6000',
    '#ffb224',
    '#f04dd5',
    '#ff6bb0',
    '#f71616',
    '#ffd324',
    '#88d600',
    '#03a60e',
    '#0316a6',
    'green',
    'blue',
    'red',
    'yellow',
    'orange',
    'grey'
]


class GameWindow:

    @staticmethod
    def game_window(numbers):

        table = table_of_numbers(
            numbers,
            background_color='#d6d6d6',
            text_color='#8d39fa',
            font=('Helvetica', 16)
        )

        table = [
                    [
                        Sg.Text('Picked Numbers', size=(32, 0), justification='center', font=('Helvetica', 15),
                                background_color='white', text_color='#706b75')
                    ],
                    [
                        Sg.Text('Completed: 00', justification='left', font=('Helvetica', 12), pad=((0, 130), (0, 0)),
                                background_color='white', text_color='#ff5703', key=KEY_COMPLETED, size=(12, 0)),
                        Sg.Text(f'Remaining: {len(numbers)}', justification='left', font=('Helvetica', 12),
                                background_color='white',
                                text_color='#7bc708', key=KEY_REMAINING, size=(12, 0))
                    ]
                ] + table

        table_frame = [
            [
                Sg.Frame('', table, size=(400, 100),
                         element_justification='center', background_color='white',
                         relief=Sg.RELIEF_FLAT, border_width=0, pad=((70, 0), (10, 0))),
            ],
            [
                Sg.Button('View Order', size=(15, 1), pad=((95, 0), (5, 8)), focus=False,
                          button_color=('white', '#559cf2'), border_width=0, disabled=True,
                          disabled_button_color=('#e3e3e3', '#e3e3e3'), key=KEY_VIEW_ORDER),
                Sg.Button('Validate Ticket', size=(15, 1), pad=((80, 0), (5, 8)), focus=False,
                          button_color=('white', '#559cf2'), border_width=0, disabled=True,
                          disabled_button_color=('#e3e3e3', '#e3e3e3'), key=KEY_VAL_TICKET)
            ]
        ]
        current = [
            [
                Sg.Text(
                    "Let us start, shall we?",
                    text_color='black',
                    background_color='#e3e3e3',
                    auto_size_text=True,
                    justification='center',
                    font=('Helvetica', 13),
                    size=(35, 1),
                    key=KEY_POP_HEAD,
                    pad=((0, 0), (10, 10))
                )
            ],
            [
                Sg.Text(
                    '',
                    key=KEY_POP,
                    text_color='green',
                    background_color='#e3e3e3',
                    auto_size_text=True,
                    justification='center',
                    font=('Helvetica', 100),
                    size=(4, 0)
                ),
            ],
            [
                Sg.Text(
                    '',
                    text_color='black',
                    background_color='#e3e3e3',
                    auto_size_text=True,
                    justification='center',
                    font=('Helvetica', 13),
                    size=(20, 1),
                    key=KEY_HIST_HEAD,
                    pad=((0, 0), (50, 10))
                ),
            ],
            [
                Sg.Text(
                    '',
                    key=KEY_HIST,
                    text_color='red',
                    background_color='#e3e3e3',
                    auto_size_text=True,
                    justification='center',
                    font=('Helvetica', 16),
                    size=(35, 1)
                )
            ],
            [
                Sg.Button('Start', size=(15, 1), key=KEY_NEXTNUM, button_color=('white', '#05a354'),
                          focus=True, border_width=0, disabled_button_color=('white', '#9effcf'),
                          pad=((10, 0), (70, 0))),
                Sg.Button('Auto Play', size=(15, 1), key=KEY_AUTO_PLAY, button_color=('white', '#05a354'),
                          focus=True, border_width=0, disabled_button_color=('white', '#9effcf'),
                          pad=((10, 0), (70, 0))),
                Sg.Button('End Game', size=(15, 1), pad=((22, 0), (70, 0)), focus=False,
                          button_color=('white', '#c70000'), border_width=0, key=KEY_ENDGAME)
            ]
        ]

        layout = [
            [
                Sg.Button("Settings", key=KEY_SETTINGS, button_color=('#9343c4', "white"), border_width=0,
                          pad=((0, 0), (0, 0)))
            ],
            [
                Sg.Column(current, background_color='#e3e3e3', size=(450, 500), element_justification='center'),
                Sg.Column(table_frame, size=(550, 500), element_justification='left', background_color='#e3e3e3')
            ]

        ]
        window = Sg.Window(
            'Tambola House', layout,
            size=default_window_size, disable_close=True,
            background_color='white',
            element_justification='center',
            resizable=True,
            text_justification='right'

        )
        return window

    def __init__(self, settings):
        self.settings = settings
        self.game = Game()
        self.window = self.game_window(self.game.nums)
        self.first_itr = True

    def run(self):
        game_completed = False
        while True:
            event, value = self.window.read()
            if event == KEY_SETTINGS:
                self.settings = SettingsWindow(self.settings).run()
            elif event == KEY_ENDGAME:
                if game_completed:
                    break
                else:
                    if EndGamePrompt().end_game():
                        break
            elif event == KEY_NEXTNUM:
                game_completed = self.update_game()
            elif event == KEY_VIEW_ORDER:
                ViewOrder(self.game.history).view_order()
            elif event == KEY_VAL_TICKET:
                ValidateTicket(self.game.history).validate()
            elif event == KEY_AUTO_PLAY:
                self.auto_play()

        self.window.close()
        return self.settings

    def disable_enable_autoplay_buttons(self, disable=True):
        self.window[KEY_NEXTNUM].update(disabled=disable)
        self.window[KEY_ENDGAME].update(disabled=disable)
        self.window[KEY_VIEW_ORDER].update(disabled=disable)
        self.window[KEY_VAL_TICKET].update(disabled=disable)

    def auto_play(self):
        self.window[KEY_AUTO_PLAY].update('Pause')
        self.disable_enable_autoplay_buttons()
        while True:
            event, value = self.window.read(1500)

            if event == KEY_AUTO_PLAY:
                break
            else:
                self.update_game()
                self.disable_enable_autoplay_buttons()

        self.disable_enable_autoplay_buttons(False)
        self.window[KEY_AUTO_PLAY].update('Auto Play')

    def blink_text(self, key, n_times=4, new_value=None, background_color='white', text_color='#8d39fa'):
        text_element = self.window[key]
        if new_value is not None:
            text_element.update(new_value)

        for i in range(0, n_times):
            text_element.update(text_color=background_color, background_color=text_color)
            self.window.read(timeout=100)
            text_element.update(text_color=text_color, background_color=background_color)
            self.window.read(timeout=100)

    def read_number(self, number):
        if self.settings.read:
            mixer.init()
            folder = SLOW_VOICE_DIR if self.settings.read_slow else FAST_VOICE_DIR
            mixer.music.load(f'{str(folder)}/{number}.mp3')
            mixer.music.play()

    def make_sound(self):
        if self.settings.sound:
            mixer.init()
            mixer.music.load(str(BELL_SOUND_FILE))
            mixer.music.play()

    def update_game(self):
        if self.first_itr:
            self.window[KEY_NEXTNUM].update('Next Number')

        self.make_sound()
        self.window[KEY_NEXTNUM].update(disabled=True)
        pop = self.game.next()
        self.window[KEY_POP_HEAD].update(random.choice(luck_liners))
        last_10_numbers = self.game.get_last_n_numbers()
        if len(last_10_numbers) > 0:
            self.window[KEY_HIST_HEAD].update(f'Last {len(last_10_numbers)} Numbers')
            self.window[KEY_HIST].update(last_10_numbers)
        pop_key = f'{pop}' if pop > 9 else f'0{pop}'

        self.blink_text(KEY_POP, new_value=str(pop), background_color='#e3e3e3',
                        text_color=random.choice(colors))
        if self.settings.read:
            self.read_number(pop_key)

        self.blink_text(f'-{pop_key}-', background_color='#8d39fa', text_color='white')

        self.window[KEY_COMPLETED].update(f'Completed: {len(self.game.history)}')
        self.window[KEY_REMAINING].update(f'Remaining: {90 - len(self.game.history)}')
        if self.settings.read:
            time.sleep(1)
        self.window[KEY_NEXTNUM].update(disabled=False)

        if self.first_itr:
            self.window[KEY_VIEW_ORDER].update(disabled=False)
            self.window[KEY_VAL_TICKET].update(disabled=False)
            self.first_itr = False

        game_completed = not self.game.numbers_exists()
        if game_completed:
            self.window[KEY_NEXTNUM].update(disabled=True, visible=False)
            self.window[KEY_POP_HEAD].update("!! Game Completed !!", text_color='Red')
            self.window.read()

        return game_completed
