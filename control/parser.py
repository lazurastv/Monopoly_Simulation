def parse(player_input):
    player_input = player_input.split()
    for i in range(len(player_input)):
        try:
            player_input[i] = int(player_input[i])
        except ValueError:
            continue
    command = player_input[0]
    args = player_input[1:]
    return command, args


class WrongCommandError(Exception):
    pass


class Parser:
    def __init__(self, command_mapping):
        self.commands = command_mapping
        self.commands["help"] = self.help

    def parse_input(self, text):
        command, args = parse(text)
        try:
            self.run(command, args)
        except WrongCommandError:
            print("Wrong command!")
        except TypeError or ValueError:
            print("Wrong arguments!")

    def run(self, command, args):
        if command not in self.commands:
            raise WrongCommandError
        self.commands[command](*args)

    def help(self):
        print(*self.commands.keys())
