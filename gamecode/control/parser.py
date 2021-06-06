def parse(player_input):
    player_input = player_input.split()
    if len(player_input) == 0:
        return 0, 0
    for i in range(len(player_input)):
        try:
            player_input[i] = int(player_input[i])
        except ValueError:
            continue
    command = player_input[0]
    args = player_input[1:]
    return command, args


class ParserError(Exception):
    pass


class Parser:
    def __init__(self, command_mapping):
        self.commands = command_mapping
        self.commands["help"] = self.help

    def parse_input(self, text):
        command, args = parse(text)
        return self.run(command, args)

    def run(self, command, args):
        try:
            self.commands[command](*args)
        except (KeyError, TypeError, ValueError):
            raise ParserError

    def help(self):
        print(*self.commands.keys())
