import math
import PySimpleGUI as Sg


def table_of_numbers(num_list, text_color='white', background_color='#60009c', font=('Helvetica', 13)):
    sqr = math.ceil(math.sqrt(len(num_list)))
    n_rows = len(num_list) // sqr
    rem = len(num_list) % sqr

    def get_hist_text(num):
        return f'{num}' if num > 9 else f'0{num}'

    table = [
        [
            Sg.Text(
                get_hist_text(num_list[i + j]), text_color=text_color,
                background_color=background_color,
                font=font,
                key=f'-{get_hist_text(num_list[i + j])}-'
            ) for j in range(0, sqr)
        ]
        for i in range(0, n_rows * sqr, sqr)
    ]
    reminder_row = [
        Sg.Text(
            get_hist_text(num_list[i]), text_color=text_color,
            background_color=background_color,
            font=font,
            key=f'-{get_hist_text(num_list[i])}-'
        )
        for i in range(n_rows * sqr, n_rows * sqr + rem)
    ]
    table.append(reminder_row)
    return table
