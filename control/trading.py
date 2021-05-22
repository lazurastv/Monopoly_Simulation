from gameplay.trade import Trade, TradeException


class Trading:
    def __init__(self):
        self.trade = None

    def load(self, player_1, player_2, diff, tiles):
        if player_1 == player_2:
            print("You cannot trade with yourself!")
            return
        try:
            self.trade = Trade(player_1, player_2, diff, tiles)
        except TradeException:
            print(TradeException)
        except ValueError:
            print("Wrong arguments!")

    def accept(self, player):
        try:
            self.trade.accept(player)
        except TradeException:
            print(TradeException)
        except AttributeError:
            print("No trade loaded!")

    def refuse(self, player):
        try:
            if player != self.trade.player_1 and player != self.trade.player_2:
                print("You cannot make decisions on this trade!")
            else:
                self.trade = None
        except AttributeError:
            print("No trade loaded!")
