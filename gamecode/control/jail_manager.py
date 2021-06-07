from gamecode.tiles.jail import JailError


class JailManager:
    def __init__(self, turn_mgr):
        self.turn_mgr = turn_mgr
        self.jail = turn_mgr.game.get_tile("Jail")

    def put_in_jail(self, player):
        self.jail.put_in_jail(player)

    def use_card(self):
        if not self.turn_mgr.can_roll:
            raise JailError("Card must be used before throwing!")
        else:
            current_player = self.turn_mgr.get_current_player()
            self.jail.use_jail_card(current_player)

    def buy_out(self):
        if not self.turn_mgr.can_roll:
            raise JailError("Buy out must happen before roll!")
        else:
            current_player = self.turn_mgr.get_current_player()
            self.jail.buy_out(current_player)
