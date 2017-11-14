from core import board, ui, validate, placement, ai, game

if __name__ == "__main__":
    comp_board = board.Board()
    human_board = board.Board()
    ui = ui.TerminalUi()
    validate = validate.Validate()
    place = placement.Place()
    ai = ai.Ai(validate)
    game = game.Game(comp_board, human_board, ai, ui, validate, place)
    game.play()
