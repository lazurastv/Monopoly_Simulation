from gamecode.gameplay.game import Game

game_a = Game()
winners = [0] * 4
for i in range(100):
    game = game_a.copy()
    game.start()
    winners[game.winner] += 1
    print(winners)