from copy import deepcopy

from gamecode.gameplay.game import Game

game_a = Game()
game_b = deepcopy(game_a)
game_a.start()
