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

    def test_play_runs_the_correct_methods(self):
        ui = TerminalUi()
        human_board = Board()
        comp_board = Board()
        board_helper = BoardHelper(comp_board.all_ships)
        validate = Validate()
        place = Place()
        ai = Ai(validate)

        board_state = [[None]]
        board_state_after_ship_placed = [['AC', 'AC', 'AC', 'AC', 'AC']]
        user_shot_choice = 'A1'
        ship_orientation = 'row'
        shot_result = 'Hit'
        current_ship = {'name': 'Aircraft Carrier', 'size': 5, 'hit_locations': [[0, 0]]}

        comp_board = MagicMock()
        comp_board.state = MagicMock(return_value=board_state)
        comp_board.add_to_board = MagicMock(return_value=board_state_after_ship_placed)
        comp_board.update = MagicMock()
        comp_board.all_ships = MagicMock(return_value=board_helper.all_ships)
        validate.spot_occupied = MagicMock(return_value=user_shot_choice)
        validate.all_ships_sunk = MagicMock()
        validate.side_effect = [False, True]
        validate.shot_result = MagicMock(return_value=('Hit', current_ship))
        ai.shoot_at_board = MagicMock(return_value=('Hit', current_ship))
        ui.get_input = MagicMock(return_value=user_shot_choice)
        ui.display = MagicMock()
        ui.terminal_board = MagicMock()
        ui.ship_messages = MagicMock()

        new_game = Game(comp_board, human_board, ai, ui, validate, place)
        new_game.play()

        comp_board.add_to_board.assert_called_with(place, ship_orientation)
        ui.display.assert_called_with(ui.terminal_board(comp_board))
        validate.spot_occupied.assert_called_with(comp_board, user_shot_choice)
        '''
        validate.shot_result.assert_called_with(comp_board, user_shot_choice)
        comp_board.update.assert_called_with(user_shot_choice, shot_result)
        '''
        validate.all_ships_sunk.assert_called()
        ai.shoot_at_board.assert_called_with(human_board)
        ui.terminal_board.assert_called()
        ui.ship_messages.assert_called()
        
    @patch('core.validate.Validate.spot_is_legal', side_effect=[False, True])
    @patch('core.ui.TerminalUi.get_input', side_effect=['A2'])
    def test_human_player_returns_the_shot_result_and_ship(self, mocks):
        board_helper = BoardHelper(comp_board.all_ships)
        validate = Validate()
        all_but_one = board_helper.generate_all_but_one()
        board = MagicMock(state=all_but_one, all_ships=self.board.all_ships)
        
