from .card import Card
from .deck import CARD_UNIVERSE, VALUES
from .functions import display_cards, probability_color_distribution
from typing import Optional
from .stock import Stock  # Import only for type checking

class Hand(list):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.stock = None  # We first set this variable after putting down a stock

    def pickup_cards(self, cards: list[Card]) -> None:
        self.extend(cards)
        self.sort_cards()

    def sort_cards(self) -> None:
        try:
            self.sort(key=lambda x: CARD_UNIVERSE.index(str(x)))
        except ValueError as e:
            print(CARD_UNIVERSE)
            raise e

    def pickup_stock(self, stock: Stock) -> None:
        """ Picks up two cards and adds them to the cards list, then sorts the list. """
        # Pickup cards from stock
        card1, card2 = stock.pickup()

        if stock.current_hand is not None:
            stock.current_hand.unlink_with_stock()
            stock.current_hand = None

        # Put the cards in their places and sort the hand
        self.append(card1)
        self.append(card2)
        self.sort_cards()

    def put_down_stock(self, index1: int, index2: int, stock: Stock) -> None:
        """ Pops and returns two cards by their index numbers. """
        if len(self) != 12:
            raise ValueError("Nem nálam van a sok!")

        # Sort the indices to ensure the higher index is processed first
        index1, index2 = sorted((index1, index2))

        # Pop the two cards from the cards list
        card1 = self.pop(index2)  # Pop the higher index first
        card2 = self.pop(index1)  # Then pop the lower index

        # Put the cards into the stock
        stock.put_down(card1, card2)

        # Link with stock
        self.link_with_stock(stock)

    def show(self) -> None:
        display_cards(self)

    def link_with_stock(self, stock: Stock) -> None:
        """ Links the hand with the given stock. """
        stock.current_hand = self
        self.stock = stock  # Store a reference to the stock

    def unlink_with_stock(self) -> None:
        """ Undo the already existing link with stock. """
        self.stock = None

    def calculate_color_probability(self, color: str) -> dict[str, float]:
        color_count_in_hand = sum(1 for card in [*self, *self.stock] if card.color == color)
        remaining_color_cards = len(VALUES) - color_count_in_hand

        # Prepare probabilities dictionary
        probabilities = {
            f"{i} - {remaining_color_cards - i}": probability_color_distribution(remaining_color_cards, i)
            for i in range(0, int((remaining_color_cards) / 2) + 1)
        }

        return probabilities