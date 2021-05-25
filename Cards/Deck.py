from random import randint

from cards.specific.get_out import GetOut
from cards.specific.go_back import GoBack
from cards.specific.group_money import GroupMoney
from cards.specific.money import Money
from cards.specific.move import Move
from cards.specific.pay_hotel import PayHotel
from cards.specific.special_move import SpecialMove
from data.file_loader import FileLoader


class Deck:
    matches = {
        "move": Move,
        "money": Money,
        "group_money": GroupMoney,
        "pay_hotel": PayHotel,
        "special_move": SpecialMove,
        "get_out": GetOut,
        "go_back": GoBack
    }

    def __init__(self, decktype):
        self.cards = []
        self.next = 0
        self.load(decktype)
        self.shuffle()

    def shuffle(self):
        n = len(self.cards)
        for i in range(n):
            j = randint(0, n - 1)
            tmp = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = tmp

    def draw(self):
        card = self.cards[self.next].copy()
        self.next += 1
        self.next %= len(self.cards)
        return card

    def load(self, decktype):
        data = FileLoader().get(decktype)
        for name in data:
            try:
                if data[name]:
                    new_card = Deck.matches[name]()
                    self.cards.append(new_card)
            except TypeError:
                for card_data in data[name]:
                    new_card = None
                    try:
                        new_card = Deck.matches[name](card_data)
                    except TypeError:
                        new_card = Deck.matches[name](**card_data)
                    finally:
                        self.cards.append(new_card)
