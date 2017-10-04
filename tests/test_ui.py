from unittest import TestCase
from core import ui

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
