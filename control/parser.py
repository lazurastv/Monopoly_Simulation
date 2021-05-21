def parse(player_input):
    player_input = player_input.split()
    command = player_input[0]
    args = player_input[1:]
    for i in range(len(args)):
        try:
            args[i] = int(args[i])
        except ValueError:
            continue
    return command, args
