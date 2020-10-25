import PySimpleGUI as Sg
from helpers.layout_helpers import table_of_numbers


class ViewOrder:

    @staticmethod
    def get_window(history):
        table = table_of_numbers(history)
        layout = [
            [
                Sg.Text('Numbers were picked in following order',
                        justification='center', font=('Helvetica', 15), background_color='#e3e3e3',
                        text_color='#706b75')
            ],
            [
                Sg.Frame('', table, element_justification='center', background_color='white', border_width=0)
            ],
            [
                Sg.Button('Close', button_color=('white', '#c70000'), border_width=0)
            ]
        ]

        return Sg.Window('Completed', layout, disable_close=True, background_color='#e3e3e3',
                         text_justification='center',
                         element_justification='center')

    def __init__(self, history):
        self.window = self.get_window(history.copy())

    def view_order(self):
        self.window.read()
        self.window.close()
