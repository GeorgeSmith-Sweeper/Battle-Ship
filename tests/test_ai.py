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
        shot_result = HIT
        board_with_ships = self.board_helper.generate_board_with_ships()
        self.human_board = MagicMock(state=board_with_ships, all_ships=self.human_board.all_ships)
        self.ai.choose_random_spot = MagicMock(return_value=ai_shot)
        self.validate.hit_ship = MagicMock(return_value=shot_result)

        self.ai.shoots_at_board(self.human_board, self.ui)

        self.ai.choose_random_spot.assert_called()
        self.human_board.update.assert_called_with(ai_shot, self.validate.shot_result(self.human_board, ai_shot, self.ui))

    def test_room_from_top_edge_returns_True_if_spot_is_not_on_the_edge(self):
        row = '2'

        self.assertTrue(self.ai.room_from_top_edge(row))

    def test_room_from_top_edge_returns_False_if_spot_is_on_the_edge(self):
        row = '1'

        self.assertFalse(self.ai.room_from_top_edge(row))

    def test_room_from_left_edge_returns_True_if_spot_is_not_on_the_edge(self):
        column = 'B'

        self.assertTrue(self.ai.room_from_left_edge(column))

    def test_room_from_left_edge_returns_False_if_spot_is_on_the_edge(self):
        column = 'A'

        self.assertFalse(self.ai.room_from_left_edge(column))

    def test_room_from_bottom_edge_returns_True_if_spot_is_not_on_the_edge(self):
        empty_board = self.board_helper.generate_empty_board()
        self.human_board = MagicMock(state=empty_board)
        row = '9'

        self.assertTrue(self.ai.room_from_bottom_edge(row, self.human_board.state))

    def test_room_from_bottom_edge_returns_False_if_spot_is_on_the_edge(self):
        empty_board = self.board_helper.generate_empty_board()
        self.human_board = MagicMock(state=empty_board)
        row = '10'

        self.assertFalse(self.ai.room_from_bottom_edge(row, self.human_board.state))

    def test_room_from_right_edge_returns_True_if_spot_is_not_the_end_of_row(self):
        empty_board = self.board_helper.generate_empty_board()
        self.human_board = MagicMock(state=empty_board)
        column = 'I'

        self.assertTrue(self.ai.room_from_right_edge(column, self.human_board.state))

    def test_room_from_right_edge_returns_False_if_spot_is_at_end_of_row(self):
        empty_board = self.board_helper.generate_empty_board()
        self.human_board = MagicMock(state=empty_board)
        column = 'J'

        self.assertFalse(self.ai.room_from_right_edge(column, self.human_board.state))

    def test_get_spot_above_returns_the_space_above_selected_spot(self):
        column = 'B'
        row = '2'

        self.assertEqual(self.ai.get_spot_above(column, row), 'B1')

    def test_get_spot_below_returns_the_space_below_selected_spot(self):
        column = 'B'
        row = '2'

        self.assertEqual(self.ai.get_spot_below(column, row, self.board.state), 'B3')

    def test_get_spot_below_returns_selected_spot_if_there_is_no_space_below(self):
        column = 'B'
        row = '10'

        self.assertEqual(self.ai.get_spot_below(column, row, self.board.state), 'B10')

    def test_get_spot_to_left_returns_the_space_to_the_left_of_selected_spot(self):
        column = 'B'
        row = '2'

        self.assertEqual(self.ai.get_spot_to_left(column, row), 'A2')

    def test_get_spot_to_right_returns_the_space_to_the_right_of_selected_spot(self):
        column = 'B'
        row = '2'

        self.assertEqual(self.ai.get_spot_to_right(column, row, self.board.state), 'C2')

    def test_get_spot_to_right_returns_selected_spot_if_there_is_no_spot_to_right(self):
        column = 'J'
        row = '10'

        self.assertEqual(self.ai.get_spot_below(column, row, self.board.state), 'J10')

    def test_remove_none_from_list_returns_a_list_without_nones(self):
        list_with_nones = ['B1', 'B2', None, None]
        list_without_nones = ['B1', 'B2']
        result = self.ai.remove_none_from_list(list_with_nones)

        self.assertEqual(result, list_without_nones)

    def test_get_surrounding_spots_adds_the_spots_to_the_next_shot_list(self):
        selected_spot = 'B2'
        correct_spots = ['B1', 'B3', 'A2', 'C2']
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
