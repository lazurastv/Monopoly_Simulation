from Tiles.Tile import Tile


class Jail(Tile):
    def __init__(self):
        super().__init__("Jail", 10)
        self.jailed_players = []

    def event(self, player):
        pass

    def put_in_jail(self, player):
        player.move_to(10)
        self.jailed_players.append(player)

    def buy_out(self, player):
        if player.has(100):
            player.pay(100)
            self.jailed_players.remove(player)

    def use_jail_card(self, player):
        if player.has_jail_card():
            player.use_jail_card()
            self.jailed_players.remove(player)

    def rolled_doubles(self, player, dice):
        if dice.repeats == 1:
            self.jailed_players.remove(player)
