from cards.card import Card


class PayHotel(Card):
    def __init__(self, house_price, hotel_price):
        self.house_price = house_price
        self.hotel_price = hotel_price

    def action(self, game, player):
        houses, hotels = player.get_house_hotel_count()
        total = self.house_price * houses + self.hotel_price * hotels
        player.pay(total)