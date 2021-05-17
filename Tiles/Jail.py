from Player import Player
from Tiles.Tile import Tile


class Jail(Tile):
    fee = 50

    def __init__(self, index):
        super().__init__("Jail")
        self.index = index
        self.jailed_players = {}

    def __contains__(self, player):
        return player is Player and player in self.jailed_players.keys()

    def starting_from_event(self, player, dice):
        if player in self:
            if self.jailed_players[player] < 3 and not self.rolled_doubles(player, dice):
                return
            self.remove_from_jail(player)
        player.move(dice.value)

    def put_in_jail(self, player):
        player.move_to(self.index)
        self.jailed_players[player] = 0

    def remove_from_jail(self, player):
        self.jailed_players.pop(player)

    def buy_out(self, player):
        if player.has(Jail.fee):
            player.pay(Jail.fee)
            self.remove_from_jail(player)

    def use_jail_card(self, player):
        if player.has_jail_card():
            player.use_jail_card()
            self.remove_from_jail(player)

    def rolled_doubles(self, player, dice):
        if dice.repeats == 1:
            return True
        else:
            self.jailed_players[player] += 1
            return False
