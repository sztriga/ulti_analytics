from .card import Card
from itertools import product
from random import shuffle


COLORS = ("P", "T", "Z", "M")
VALUES = ("X", "K", "F", "A") + tuple(range(10, 6, -1))
CARD_PRODUCT = [(color, value) for color, value in product(COLORS, VALUES)]
CARD_UNIVERSE = [color + str(value) for color, value in CARD_PRODUCT]

class Deck:
    def __init__(self):
        self.cards = []
    
        # Setup a regular ulti deck
        for color, value in CARD_PRODUCT:
            self.cards.append(Card(color=color, value=value))
            
    def shuffle(self) -> None:
        shuffle(self.cards)
        
    def deal(self) -> tuple[list[Card]]:
        self.shuffle()
        return (self.cards[:12], self.cards[12:22], self.cards[22:])