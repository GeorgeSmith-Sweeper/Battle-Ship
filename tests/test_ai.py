from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ui import TerminalUi
from core.validate import Validate
from core.ships import Ships
from helpers.board_helper import BoardHelper
from core.ai import Ai

class TestAi(TestCase):

    def test_ai_shoots_at_board_runs_the_correct_methods(self):
        ships = Ships()
        validate = Validate()
        board_helper = BoardHelper(ships)
        human_board = Board(ships)
        ui = TerminalUi()
        ai = Ai(validate)
        
        ai_shot = 'A2'
        shot_result = 'Hit' 
        board_with_ships = board_helper.generate_board_with_ships()
        board_after_ai_shot = board_helper.generate_board_with_hit()

        human_board.state = MagicMock(return_value=board_with_ships) 
        human_board.update = MagicMock()
        ai.choose_random_spot = MagicMock(return_value = ai_shot) 
        validate.hit_ship = MagicMock(return_value = 'Hit')

        ai.shoots_at_board(human_board, ui)
        
        ai.choose_random_spot.assert_called()
        human_board.update.assert_called_with(ai_shot, validate.hit_ship(human_board.state, ai_shot, human_board.ships.all_ships, ui))
    
    def test_choose_random_spot_picks_a_spot_chooses_spaces_from_available_spaces(self):
        validate = Validate()
        ai = Ai(validate)
        ships = Ships()
        board_helper = BoardHelper(ships)
        all_spots_list = board_helper.generate_all_spots()

        random_spot = ai.choose_random_spot()
        self.assertIn(random_spot, all_spots_list)
    
    @patch('core.ai.Ai.choose_random_spot', return_value='B1')
    def test_shoots_at_board_updates_the_board_to_Hit_if_it_hits_a_ship(self, mock):
        ui = TerminalUi()
        validate = Validate()
        ai = Ai(validate)
        ships = Ships()
        human_board = Board(ships)
        board_helper = BoardHelper(ships)
        all_spots_list = board_helper.generate_all_spots()
        human_board.state = board_helper.generate_board_with_ships()
        board_with_a_hit = board_helper.generate_board_with_hit()

        ai.shoots_at_board(human_board, ui)
        self.assertEqual(human_board.state, board_with_a_hit)
        
