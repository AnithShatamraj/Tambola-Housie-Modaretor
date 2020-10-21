import random
import numpy as np
import layout_render
import PySimpleGUI as Sg
from pprint import pprint


class Game:

    def __init__(self, name='My Games'):
        self.id = id
        self.name = name
        self.nums = list(range(0, 100))
        self.popped = [0] * 100
        self.pop = 0
        self.history = []

    def start(self):
        return self.pop, np.reshape(self.popped, (10, 10)).tolist(), self.history

    def next(self):
        random.shuffle(self.nums)
        self.pop = self.nums.pop()
        self.popped[self.pop - 1] = self.pop

        self.history.insert(0, self.pop)
        tab = np.reshape(self.popped, (10, 10)).tolist()

        return self.pop, tab, self.history[1:6], len(self.nums) > 0


def run():
    while True:
        home_screen = layout_render.home_screen()
        home_event, home_value = home_screen.read()
        if home_event == "New Game":
            home_screen.close()
            _game = Game()
            pop, tab, hist = _game.start()
            game_window = layout_render.game_window(pop, hist)

            running = True
            while running:
                event, value = game_window.read()
                if event == 'Next Number':
                    pop, tab, hist, running = _game.next()
                    game_window[f'-POP-'].update(str(pop))
                    pop_key = f'-{pop}-' if pop > 9 else f'-0{pop}-'
                    game_window[pop_key].update(background_color='red')
                    game_window['-HIST-'].update(hist)
                elif event == 'End Game' or event == Sg.WIN_CLOSED:
                    end_game_window = layout_render.comfirm_close()
                    close_event, close_val = end_game_window.read()
                    if close_event == 'End Game':
                        end_game_window.close()
                        break
                    end_game_window.close()
                else:
                    break

            game_window.close()

        else:
            home_screen.close()
            break


if __name__ == '__main__':
    gam = Game()
    cur_num, table, his = gam.start()
    print(cur_num)
    pprint(table)
    print(his)

    cont = True
    idx = 0
    while cont:
        idx += 1
        print('-'*100, '\n', idx, '\n', '-'*100)
        cur_num, table, his, cont = gam.next()
        print(cur_num)
        pprint(table)
        print(his)
