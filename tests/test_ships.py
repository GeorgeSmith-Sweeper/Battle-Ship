'''
class ComputerShips(TestCase):
    def test_create_ships_places_the_correct_ships_on_the_board(self):
        board = Board()
        ships = Ships()
        ship_added = Ship_Placer(board, ships)

        board_state = [[]]
        board_state_after_ship_was_added = [['AC', 'AC', 'AC', 'AC', 'AC']]

        ship.aircraft_carrier = MagicMock()
'''
