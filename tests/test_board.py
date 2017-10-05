from unittest import TestCase
from core import board 

class TestBoard(TestCase):
    def setUp(self):
        self.new_board = board.Board()

    def test_boards_are_initialized_with_state(self):
        state = [[None for x in range(10)] for y in range(10)]
        self.assertEqual(self.new_board.state, state) 
        
