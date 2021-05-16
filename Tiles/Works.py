from Tiles.Property import Property


class Works(Property):
    def __init__(self, name, price, mortgage, group=None):
        super().__init__(name, price, mortgage, group)

    def event(self, player):
        if self.owner:
            if player != self.owner:
                player.pay(self.rent(), self.owner)

    def rent(self):
        pass
