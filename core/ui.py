class TerminalUi:
    def display(self, message):
       print(message)

    def get_input(self, prompt_string):
        response = input(prompt_string)
        return response
