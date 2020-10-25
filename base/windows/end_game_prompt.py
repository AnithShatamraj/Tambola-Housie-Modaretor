import PySimpleGUI as Sg


class EndGamePrompt:

    @staticmethod
    def comfirm_close():
        layout = [
            [
                Sg.Text('Are you sure you want to end the game?',
                        background_color='#e3e3e3',
                        font=('Helvetica', 13),
                        text_color='red',
                        justification='center',
                        size=(55, 1)
                        )
            ],
            [
                Sg.Text('Press "End Game" to End the game, Press "Continue" to keep playing',
                        background_color='#e3e3e3',
                        font=('Helvetica', 12),
                        text_color='black',
                        justification='center',
                        size=(55, 1)
                        )
            ],
            [
                Sg.Button('Continue', size=(15, 1), button_color=('white', '#05a354'),
                          border_width=0),
                Sg.Button('End Game', size=(15, 1), button_color=('white', '#c70000'),
                          border_width=0)
            ]
        ]
        window = Sg.Window(
            f'!!!Confirm End Game!!!',
            layout,
            background_color='#e3e3e3',
            element_justification='center'
        )
        return window

    def __init__(self):
        self.window = self.comfirm_close()

    def end_game(self):
        event, values = self.window.read()
        self.window.close()
        return event == 'End Game'
