import PySimpleGUI as Sg
import re
from helpers.layout_helpers import table_of_numbers


class ValidateTicket:

    @staticmethod
    def validate_window(history):

        hist_tab = table_of_numbers(history, text_color='orange', background_color='white', font=('Helvetica', 15))

        layout = [
            [
                Sg.Frame('Picked Numbers', hist_tab, background_color='#e3e3e3', title_color='black')
            ],
            [
                Sg.Text('', key='-output-', size=(30, 0), font=('Helvetica', 15), background_color='#e3e3e3')
            ],
            [
                Sg.Text('Enter Numbers with spaces', background_color='#e3e3e3', text_color='black')
            ],
            [
                Sg.InputText(key='-message-', background_color='#e3e3e3')
            ],
            [
                Sg.Button('Validate', key='-validate-', button_color=('white', '#559cf2'), border_width=0),
                Sg.Button('Close', key='-close-', button_color=('white', '#559cf2'), border_width=0)
            ]
        ]

        return Sg.Window('Validate', layout, element_justification='center', text_justification='center',
                         background_color='#e3e3e3')

    def __init__(self, history):
        self.history = history.copy()
        self.history.sort()
        self.window = self.validate_window(self.history)

    def _update_message(self, message, is_valid=False):
        if is_valid:
            text_color = '#0f992b'
        else:
            text_color = '#d60909'
        self.window['-output-'].update(message, text_color=text_color)

    def _highlight_number(self, n, background_color='green'):
        num = f'-{n}-' if n > 9 else f'-0{n}-'
        self.window[num].update(background_color=background_color)

    def _reset_table(self):
        for n in self.history:
            self._highlight_number(n, background_color='white')

    def validate_ticket(self, value):
        self._reset_table()
        text = value['-message-'].strip()
        no_match = []
        if re.match('^[0-9 ]*$', text):
            nums = text.split(' ')
            for n_s in nums:
                n_s = n_s.strip()
                n = int(n_s)
                if n > 99 or n < 0:
                    self._update_message(f'Invalid Number: {n_s}, Number should be between 0 and 99')
                else:
                    if n in self.history:
                        self._highlight_number(n)
                    else:
                        no_match.append(n_s)
            if len(no_match) > 0:
                self._update_message(f'Invalid ticket. Numbers do not exists:\n{", ".join(no_match)}')
            else:
                self._update_message('Valid, All Numbers Match', True)
        else:
            self._update_message('Invalid input, Number should be between 0 and 99 with spaces in between them')

    def validate(self):
        event, values = self.window.read()
        while event != '-close-':
            if event == '-validate-':
                self.validate_ticket(values)
            event, values = self.window.read()
        if event == Sg.WIN_CLOSED:
            self.window.close()
        self.window.close()
