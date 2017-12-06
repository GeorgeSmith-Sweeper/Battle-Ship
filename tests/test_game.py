from unittest import TestCase
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ui import TerminalUi
from core.validate import Validate
from core.placement import Place
from core.ai import Ai
from helpers.board_helper import BoardHelper
from core.game import Game


class TestPlayGame(TestCase):

    def setUp(self):
        self.ui = TerminalUi()
        self.human_board = Board()
        self.comp_board = Board()
        self.board_helper = BoardHelper(self.comp_board.all_ships)
        self.validate = Validate()
        self.ai = Ai(self.validate)
        self.place = Place()

    def test_play_runs_the_correct_methods(self):
        board_state = [[None]]
        board_state_after_ship_placed = [['AC', 'AC', 'AC', 'AC', 'AC']]
        user_shot_choice = 'A1'
        ship_orientation = 'row'
        shot_result = 'Hit'
        current_ship = {'name': 'Aircraft Carrier', 'size': 5, 'hit_locations': [[0, 0]]}

        self.comp_board = MagicMock()
        self.comp_board.state = MagicMock(return_value=board_state)
        self.comp_board.add_to_board = MagicMock(return_value=board_state_after_ship_placed)
        self.comp_board.update = MagicMock()
        self.comp_board.all_ships = MagicMock(return_value=self.board_helper.all_ships)
        self.validate = MagicMock()
        self.validate.shot_result = MagicMock(return_value=('Hit', current_ship))
        self.validate.all_ships_sunk = MagicMock(side_effect=[False, True])
        self.ai.shoot_at_board = MagicMock(return_value=('Hit', current_ship))
        self.ui.get_input = MagicMock(return_value=user_shot_choice)
        self.ui.display = MagicMock()
        self.ui.game_board = MagicMock()
        self.ui.ship_messages = MagicMock()

        new_game = Game(self.comp_board, self.human_board, self.ai, self.ui, self.validate, self.place)
        new_game.play()

        self.comp_board.add_to_board.assert_called_with(self.place, ship_orientation)
        self.ui.display.assert_called()
        self.comp_board.update.assert_called_with(user_shot_choice, shot_result)
        self.validate.all_ships_sunk.assert_called()
        self.ai.shoot_at_board.assert_called_with(self.human_board)
        self.ui.game_board.assert_called()
        self.ui.ship_messages.assert_called()

    @patch('core.validate.Validate.spot_is_legal', return_value=True)
    @patch('core.ui.TerminalUi.get_input', return_value='A1')
    def test_human_player_returns_the_shot_result_and_ship(self, mock1, mock2):
        new_game = Game(self.comp_board, self.human_board, self.ai, self.ui, self.validate, self.place)
        board_with_ships = self.board_helper.generate_board_with_ships()
        board = MagicMock(state=board_with_ships, all_ships=self.comp_board.all_ships)
        expected_ship = {
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [[0, 0]],
        }
        expected_shot_result = 'Hit'
        shot_result, ship = new_game._human_turn(board)
        self.assertEqual((expected_shot_result, expected_ship), (shot_result, ship))
