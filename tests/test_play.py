from unittest import TestCase
from unittest.mock import patch, MagicMock
from play import Game
from core import ui
from core import board

class TestGameLoop:
    def test_game_starts(self):
        with patch.object(Game, 'display_terminal_board', return_value=None) as mock_method:
            new_board = board.Board()
            new_game = Game(new_board)
            new_game.start()
            mock_method.assert_called()
             
