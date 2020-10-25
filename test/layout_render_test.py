import unittest
from windows.validate_ticket import ValidateTicket
from windows.end_game_prompt import EndGamePrompt
from windows.settings_window import SettingsWindow
from windows.home_screen import HomeScreen
from windows.game_window import GameWindow
from windows.view_order import ViewOrder
from settings import Settings


class MyTestCase(unittest.TestCase):
    def test_home_screen(self):
        HomeScreen().run()

    def test_game_screen(self):
        GameWindow(Settings()).run()

    def test_end_game(self):
        print(EndGamePrompt().end_game())

    def test_history(self):
        ViewOrder(list(range(0, 30))).view_order()

    def test_validate(self):
        ValidateTicket(list(range(0, 23))).validate()

    def test_settings(self):
        settings = SettingsWindow().run()
        print(settings.sound)
        print(settings.read)
        print(settings.read_slow)


if __name__ == '__main__':
    unittest.main()
