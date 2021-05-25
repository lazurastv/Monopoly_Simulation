from tiles.tile import Tile


class Jail(Tile):
    fee = 50

    def __init__(self, pos):
        super().__init__(pos)
        self.jailed_players = {}

    def __contains__(self, player):
        return player in self.jailed_players.keys()

    def __str__(self):
        return super().__str__() + ", jailed: " + str(self.jailed_players)

    def starting_from_event(self, player, dice):
        if player in self:
            if self.jailed_players[player] < 3 and not self.rolled_doubles(player, dice):
                return
            self.remove_from_jail(player)
        player.move(dice.value)

    def put_in_jail(self, player):
        player.move_to(self.position)
        self.jailed_players[player] = 0

    def remove_from_jail(self, player):
        self.jailed_players.pop(player)

    def buy_out(self, player):
        if player not in self:
            print("You are not in jail!")
        elif not player.has(Jail.fee):
            print("You don't have enough money for a buy out!")
        else:
            player.pay(Jail.fee)
            self.remove_from_jail(player)

    def use_jail_card(self, player):
        if player not in self:
            print("You are not in jail!")
        elif not player.has_jail_card():
            print("You don't have a jail card!")
        else:
            player.use_jail_card()
            self.remove_from_jail(player)

    def rolled_doubles(self, player, dice):
        if dice.repeats == 1:
            return True
        else:
            self.jailed_players[player] += 1
            return False
