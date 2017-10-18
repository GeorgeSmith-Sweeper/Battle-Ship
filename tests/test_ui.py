from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.ui import TerminalUi
from io import StringIO

class TestTerminalUi(TestCase):

    def test_terminal_displays_string_passed_to_it(self):
       ui = TerminalUi()
       with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
           ui.display('Welcome to Battleship')
       self.assertEqual(fake_stdout.getvalue(), 'Welcome to Battleship\n')

    def correct_response(self):
        ui = TerminalUi()
        answer = ui.get_input("Enter hello: ")
        if answer == 'hello':
            return 'it works'

    @patch('core.ui.TerminalUi.get_input', return_value='hello')
    def test_get_input_returns_a_users_input(self, mock):
        self.assertEqual(self.correct_response(), 'it works')
