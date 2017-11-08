from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ui import TerminalUi
from core.validate import Validate
from helpers.board_helper import BoardHelper
from core.ai import Ai

class TestAi(TestCase):

    def setUp(self):
        self.board = Board()
        self.validate = Validate()
        self.board_helper = BoardHelper(self.board.all_ships)
        self.human_board = Board()
        self.ui = TerminalUi()
        self.ai = Ai(self.validate)
   
    def test_ai_can_keep_track_of_its_next_shot(self):
        self.assertEqual(self.ai.next_shots_list, [])

    def test_ai_shoots_at_board_runs_the_correct_methods(self):
        ai_shot = 'A2'
        shot_result = 'Hit' 
        board_with_ships = self.board_helper.generate_board_with_ships()
        board_after_ai_shot = self.board_helper.generate_board_with_hit()
        
        self.human_board = MagicMock(state=board_with_ships, all_ships=self.human_board.all_ships)
        self.ai.choose_random_spot = MagicMock(return_value = ai_shot) 
        self.validate.hit_ship = MagicMock(return_value = 'Hit')

        self.ai.shoots_at_board(self.human_board, self.ui)

        self.ai.choose_random_spot.assert_called()
        self.human_board.update.assert_called_with(ai_shot, self.validate.hit_ship(self.human_board, ai_shot, self.ui))
    
    def test_get_spot_above_returns_the_space_above_selected_spot(self):
        letter = 'B'
        number = '2'

        self.assertEqual(self.ai.get_spot_above(letter, number), 'B1')
    
    def test_get_spot_below_returns_the_space_below_selected_spot(self):
        letter = 'B'
        number = '2'

        self.assertEqual(self.ai.get_spot_below(letter, number, self.board.state), 'B3')

    def test_get_spot_to_left_returns_the_space_to_the_left_of_selected_spot(self):
        letter = 'B'
        number = '2'

        self.assertEqual(self.ai.get_spot_to_left(letter, number), 'A2')

    def test_get_spot_to_right_returns_the_space_to_the_right_of_selected_spot(self):
        letter = 'B'
        number = '2'

        self.assertEqual(self.ai.get_spot_to_right(letter, number, self.board.state), 'C2')

    def test_get_surrounding_spots_adds_the_spots_to_the_next_shot_list(self):
        selected_spot = 'B2'
        correct_spots = ['B1', 'A2', 'B3', 'C2']
        self.ai.get_surrounding_spots(selected_spot, self.human_board.state)
        
        self.assertEqual(self.ai.next_shots_list, correct_spots)
        
    def test_choose_random_spot_picks_a_spot_chooses_spaces_from_available_spaces(self):
        all_spots_list = self.board_helper.generate_all_spots()

        random_spot = self.ai.choose_random_spot()
        self.assertIn(random_spot, all_spots_list)
   
    def test_intelligent_shot_updates_the_board_with_shots_from_nxt_shot_list(self):
        self.ai.next_shots_list = ['B1']
        board_with_a_hit = self.board_helper.generate_board_with_hit()
        self.board.state = self.board_helper.generate_board_with_ships()
        
        self.ai.intelligent_shot(self.board, self.ui)
        self.assertEqual(self.board.state, board_with_a_hit)

    @patch('core.ai.Ai.choose_random_spot', return_value='B1') 
    def test_random_shot_updates_the_board_with_a_random_shot(self, mock):
        board_with_a_hit = self.board_helper.generate_board_with_hit()
        self.board.state = self.board_helper.generate_board_with_ships()
        
        self.ai.random_shot(self.board, self.ui)
        self.assertEqual(self.board.state, board_with_a_hit)

    def test_shoots_at_board_updates_the_board_to_Hit_if_it_hits_a_ship(self):
        all_spots_list = self.board_helper.generate_all_spots()
        self.human_board.state = self.board_helper.generate_board_with_ships()
        board_with_a_hit = self.board_helper.generate_board_with_hit()

        self.ai.shoots_at_board(self.human_board, self.ui)
