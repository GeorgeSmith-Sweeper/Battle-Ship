from unittest import TestCase
from core import board 

class TestBoard(TestCase):
    def test_boards_are_initialized_with_state(self):
        new_board = board.Board()
        state = [[None for x in range(10)] for y in range(10)]
        self.assertEqual(new_board.state, state) 
