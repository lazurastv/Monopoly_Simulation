from random import random

from gamecode.tiles.tile import Tile


class JailError(Exception):
    pass


class Jail(Tile):
    FEE = 50

    def __init__(self, pos):
        super().__init__(pos)
        self.jailed_players = {}
        self.id = random()

    def __str__(self):
        return super().__str__() + ", jailed: " + str(self.jailed_players)

    def __contains__(self, item):
        return item in self.jailed_players

    def __iter__(self):
        return iter(self.jailed_players)

    def copy(self, game):
        jail_copy = Jail(self.position)
        for player in self:
            player_copy = game.get_player_by_id(player.id)
            player_copy.in_jail = True
            jail_copy.jailed_players[player_copy] = self.jailed_players[player]
        return jail_copy

    def starting_from_event(self, player, dice):
        if player in self.jailed_players:
            if self.jailed_players[player] < 3 and not self.rolled_doubles(player, dice):
                return
            self.remove_from_jail(player)
        player.move(dice.value())

    def put_in_jail(self, player):
        player.in_jail = True
        player.move_to(self.position)
        self.jailed_players[player] = 0

    def turns_left(self, player):
        return 3 - self.jailed_players[player]

    def remove_from_jail(self, player):
        player.in_jail = False
        self.jailed_players.pop(player)

    def buy_out(self, player):
        if not player.in_jail:
            raise JailError("You are not in jail!")
        elif not player.has(Jail.FEE):
            raise JailError("You don't have enough money for a buy out!")
        else:
            player.pay(Jail.FEE)
            self.remove_from_jail(player)

    def use_jail_card(self, player):
        if player not in self:
            raise JailError("You are not in jail!")
        elif not player.has_jail_card():
            raise JailError("You don't have a jail card!")
        else:
            player.use_jail_card()
            self.remove_from_jail(player)

    def rolled_doubles(self, player, dice):
        if dice.repeats == 1:
            return True
        else:
            self.jailed_players[player] += 1
            return False
