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
