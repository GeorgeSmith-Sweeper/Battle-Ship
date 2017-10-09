from unittest import TestCase, mock
from unittest.mock import patch
from core import ui
from io import StringIO

class TestPrintWrapper(TestCase):
    def test_strings_passed_to_console_msg_print(self):
        message = ui.Messages()
        with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
            message.terminal_msg('hello')
        self.assertEqual(fake_stdout.getvalue(), 'hello\n')

class TestInputWrapper(TestCase):
    def answer(self):
        prompt = ui.Messages()
        testAnswer = prompt.prompt_user("enter hello")
        if testAnswer == 'hello':
            return 'it works'
        
    @patch('core.ui.Messages.prompt_user', return_value="hello")
    def test_can_get_input(self, imput):
        self.assertEqual(self.answer(), 'it works')

class TestDisplayBoard(TestCase):
    def test_board_is_displayed_as_a_grid(self):
        empty_board = """
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
"""
        board_state = [[None for ele in range(10)] for index in range(10)]
        board = ui.BoardPresenter()
        self.assertEqual(board.display_terminal_board(board_state), empty_board)
