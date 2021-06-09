from gamecode.gameplay.game import Game

winners = [0] * 10
while True:
    game = Game()
    game.start()
    winner_value = game.get_player(0).logic.risk_factor
    winners[int(winner_value * 10)] += 1
    print(winners)
