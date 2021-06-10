from gamecode.gameplay.game import Game


def winner_risk_factor_distribution(amount=100):
    winners = [0] * 10
    for i in range(amount):
        game = Game()
        game.start()
        winner_value = game.winner.logic.risk_factor
        winners[int(winner_value * 10)] += 1
        print(i, winners)
    for i in range(10):
        print("Risk factor <", 0.1 * i, ",", 0.1 + 0.1 * i, "> won", winners[i] / amount * 100, "% of games")


def monte_carlo_showcase(amount=100):
    game = Game()
    target = 0
    wins_without_extra_tiles = 0
    wins_with_extra_tiles = 0
    for i in range(amount):
        game_without_extra_tiles = game.copy()
        me = game_without_extra_tiles.get_player_by_id(target)
        game_without_extra_tiles.start()
        if game_without_extra_tiles.winner is me:
            wins_without_extra_tiles += 1
        game_with_extra_tiles = game.copy()
        me = game_with_extra_tiles.get_player_by_id(target)
        game_with_extra_tiles.get_tile(37).change_owner(me)
        game_with_extra_tiles.get_tile(39).change_owner(me)
        game_with_extra_tiles.start()
        if game_with_extra_tiles.winner is me:
            wins_with_extra_tiles += 1
        print(i, wins_without_extra_tiles, wins_with_extra_tiles)
    print("Probability to win without extra tiles:", wins_without_extra_tiles / amount * 100, "%")
    print("Probability to win with extra tiles:", wins_with_extra_tiles / amount * 100, "%")
    print("Your risk factor was", game.get_player_by_id(target).logic.risk_factor)


if __name__ == "__main__":
    winner_risk_factor_distribution()
    monte_carlo_showcase()
