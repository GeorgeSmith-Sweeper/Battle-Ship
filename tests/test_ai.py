from unittest import TestCase
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ui import TerminalUi
from core.validate import Validate
from helpers.board_helper import BoardHelper
from helpers.constants import HIT
from core.ai import Ai


class TestAi(TestCase):

    def setUp(self):
        self.board = Board()
        self.validate = Validate()
        self.board_helper = BoardHelper(self.board.all_ships)
        self.human_board = Board()
        self.ui = TerminalUi()
        self.ai = Ai(self.validate)

    def test_ai_shoots_at_board_runs_the_correct_methods(self):
        ai_shot = 'A2'
        result = (HIT, {'name': 'Aircraft Carrier', 'size': 5, 'hit_locations': [[0, 0]]})
        shot_result, current_ship = result
        board_with_ships = self.board_helper.generate_board_with_ships()
        self.human_board = MagicMock(state=board_with_ships, all_ships=self.human_board.all_ships)
        self.ai._choose_random_spot = MagicMock(return_value=ai_shot)
        self.validate.shot_result = MagicMock(return_value=result)
        self.ai.shoot_at_board(self.human_board)
        
        self.ai._choose_random_spot.assert_called()
        self.human_board.update.assert_called_with(ai_shot, shot_result)

    def test_legal_spot_returns_the_spot_if_it_exists(self):
        spot = 'A1'
        self.assertEqual(spot, self.ai._legal_space(spot))

    def test_legal_spot_returns_None_if_spot_does_not_exist(self):
        spot = 'Z1'
        self.assertEqual(None, self.ai._legal_space(spot))
        
    def test_remove_none_from_list_returns_a_list_without_nones(self):
        list_with_nones = ['B1', 'B2', None, None]
        list_without_nones = ['B1', 'B2']
        result = self.ai._remove_none_from_list(list_with_nones)

        self.assertEqual(result, list_without_nones)

    def test_get_surrounding_spots_adds_the_spots_to_the_next_shot_list(self):
        selected_spot = 'B2'
        correct_spots = ['B1', 'B3', 'A2', 'C2']
        self.ai._get_surrounding_spots(selected_spot)

        self.assertEqual(self.ai.next_shots_list, correct_spots)

    def test_get_surrounding_spots_at_upper_left_corner(self):
        selected_spot = 'A1'
        correct_spots = ['A2', 'B1']
        self.ai._get_surrounding_spots(selected_spot)

        self.assertEqual(self.ai.next_shots_list, correct_spots)

    def test_get_surrounding_spots_at_upper_right_corner(self):
        selected_spot = 'J1'
        correct_spots = ['J2', 'I1']
        self.ai._get_surrounding_spots(selected_spot)

        self.assertEqual(self.ai.next_shots_list, correct_spots)

    def test_get_surrounding_spots_at_bottom_right_corner(self):
        selected_spot = 'J10'
        correct_spots = ['J9', 'I10']
        self.ai._get_surrounding_spots(selected_spot)

        self.assertEqual(self.ai.next_shots_list, correct_spots)

    def test_get_surrounding_spots_at_bottom_left_corner(self):
        selected_spot = 'A10'
        correct_spots = ['A9', 'B10']
        self.ai._get_surrounding_spots(selected_spot)

        self.assertEqual(self.ai.next_shots_list, correct_spots)

    def test_get_surrounding_spots_at_bottom_edge_returns_current_spot(self):
        selected_spot = 'B10'
        correct_spots = ['B9', 'A10', 'C10']
        self.ai._get_surrounding_spots(selected_spot)
        
        self.assertEqual(self.ai.next_shots_list, correct_spots)

    def test_choose_random_spot_picks_a_spot_chooses_spaces_from_available_spaces(self):
        all_spots_list = self.board_helper.generate_all_spots()
        random_spot = self.ai._choose_random_spot()
        
        self.assertIn(random_spot, all_spots_list)

    def test_unified_shot_updates_the_board_with_shots_from_nxt_shot_list(self):
        self.ai.next_shots_list = ['B1']
        spot = 'B1'
        board_with_a_hit = self.board_helper.generate_board_with_hit()
        self.board.state = self.board_helper.generate_board_with_ships()
        self.ai._computer_shot(self.board, spot)
        
        self.assertEqual(self.board.state, board_with_a_hit)

    @patch('core.ai.Ai._choose_random_spot', return_value='B1')
    def test_unified_shot_updates_the_board_with_a_random_shot(self, mock):
        board_with_a_hit = self.board_helper.generate_board_with_hit()
        self.board.state = self.board_helper.generate_board_with_ships()
        random_spot = 'B1'
        self.ai._computer_shot(self.board, random_spot)
        
        self.assertEqual(self.board.state, board_with_a_hit)