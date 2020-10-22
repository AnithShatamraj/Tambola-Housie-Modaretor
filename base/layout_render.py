import PySimpleGUI as Sg

default_window_size = (1000, 500)
cols = [f'Col{i}' for i in range(1, 11)]
rows = [f'Row{i}' for i in range(0, 10)],


def home_screen():
    layout = [
        [
            Sg.Text('Welcome to Tambola House',
                    background_color='white',
                    text_color='black',
                    auto_size_text=True,
                    size=(500, 2),
                    justification='center',
                    font=('Helvetica', 20)
                    )
        ],
        [
            Sg.Text('Click on New Game',
                    background_color='white',
                    text_color='black',
                    auto_size_text=True,
                    size=(500, 3),
                    justification='center',
                    font=('Helvetica', 15)
                    )
        ],
        [
            Sg.Button("New Game", pad=((392, 20), (20, 0)), size=(10, 1)),
            Sg.Button("Close", pad=((10, 0), (20, 0)), size=(10, 1))
        ]
    ]

    window = Sg.Window(
        f'Tambola',
        layout,
        background_color='white',
        size=default_window_size
    )

    return window


def game_window(pop, history):
    table = [
        [
            Sg.Text(
                f'{i}{j}', text_color='blue',
                background_color='white',
                key=f'-{i}{j}-',
                font=('Helvetica', 15)
            ) for j in range(0, 10)
        ]
        for i in range(0, 10)
    ]
    table.insert(
        0,
        [
            Sg.Text('Picked Numbers', size=(35, 0), justification='center', font=('Helvetica', 15))
        ]
    )
    table_frame = [[Sg.Frame(None, table, size=(370, 370), pad=((100, 100), (40, 0)))]]
    current = [
                    [
                        Sg.Text(
                            'Number is: ',
                            background_color='white',
                            text_color='black',
                            auto_size_text=True,
                            justification='left',
                            font=('Helvetica', 12),
                            size=(10, 1)
                        )
                    ],
                    [
                        Sg.Text(
                            str(pop),
                            key='-POP-',
                            background_color='white',
                            text_color='green',
                            auto_size_text=True,
                            justification='center',
                            font=('Helvetica', 50),
                            size=(10, 1)
                        ),
                    ],
                    [
                        Sg.Text(
                            'Last 5: ',
                            background_color='white',
                            text_color='black',
                            auto_size_text=True,
                            justification='left',
                            font=('Helvetica', 12),
                            size=(10, 1)
                        ),
                    ],
                    [
                        Sg.Text(
                            ', '.join(history),
                            key='-HIST-',
                            background_color='white',
                            text_color='red',
                            auto_size_text=True,
                            justification='left',
                            font=('Helvetica', 15),
                            size=(30, 1)
                        )
                    ],
                    [
                        Sg.Button('Next Number', size=(15, 1)),
                        Sg.Button('End Game', size=(15, 1), pad=((125, 0), (0, 0)))
                    ]
                ]

    layout = [
        [
            Sg.Column(current, background_color='white', size=(400, 500)),
            Sg.Column(table_frame, size=(600, 500), element_justification='right')
        ]

    ]
    window = Sg.Window('Tambola House', layout, size=default_window_size, disable_close=True)
    return window


def comfirm_close():
    layout = [
        [
            Sg.Text('Are you sure you want to end the game?',
                    background_color='white',
                    text_color='red',
                    justification='center',
                    size=(55, 1)
                    )
        ],
        [
            Sg.Text('Press "End Game" to End the game, Press "Continue" to keep playing',
                    background_color='white',
                    text_color='black',
                    justification='center',
                    size=(55, 1)
                    )
        ],
        [
            Sg.Button('Continue', size=(15, 1), pad=((90, 1), (0, 0))),
            Sg.Button('End Game', size=(15, 1), pad=((10, 0), (0, 0)))
        ]
    ]
    window = Sg.Window(
        f'!!!Confirm End Game!!!',
        layout,
        background_color='white'
    )
    return window


def game_completed_window(history):
    n_rows = len(history) // 10
    rem = len(history) % 10
    padding = 10 if n_rows > 1 else 10-rem
    def get_hist_text(num):
        return f'{num}' if num > 9 else f'0{num}'
    table = [
        [
            Sg.Text(
                get_hist_text(history[i+j]), text_color='blue',
                background_color='white',
                font=('Helvetica', 12)
            ) for j in range(0, 10)
        ]
        for i in range(0, n_rows*10, 10)
    ]
    remider_row = [
        Sg.Text(
            get_hist_text(history[i]), text_color='blue',
            background_color='white',
            font=('Helvetica', 12)
        )
        for i in range(n_rows*10, n_rows*10+rem)
    ]
    table.append(remider_row)
    layout = [
        [
            Sg.Text('Game End', size=(50, 0), justification='center', font=('Helvetica', 15))
        ],
        [
            Sg.Text('Numbers were picked in following order', size=(50, 0),
                    justification='center', font=('Helvetica', 15))
        ],
        [
            Sg.Frame(None, table, element_justification='center', pad=((120, 0), (0, 0)))
        ],
        [
            Sg.Button('Close', pad=((260, 0), (0, 0)))
        ]
    ]
    return Sg.Window('Completed', layout, disable_close=True)


if __name__ == '__main__':
    i = 0
    win = game_completed_window(list(range(0, 25)))
    event, value = win.read()

    win.close()