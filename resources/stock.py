from .card import Card
from .functions import display_cards


class Stock(list):
    def __init__(self):
        super().__init__()
        self.current_hand = None  # Keep track of the current hand using this stock
        
    def pickup(self) -> list[Card]:
        """ Simulates picking up the stock by a hand. """        
        # Take the cards from the stock
        cards_taken = self.copy()  # Copy the current cards
        self.clear()  # Clear the stock
        
        return cards_taken  # Return the cards that were picked up
        
    def put_down(self, card1: Card, card2: Card) -> None:
        """ Puts down two new cards into the stock. """
        self.extend([card1, card2])  # Use the update method to add the cards        

    def clear_stock(self) -> None:
        """ Clears the stock and resets the current hand. """
        self.clear()  # Clear the stock
        self.current_hand = None  # Reset current hand
        print("Stock cleared.")
        
    def show(self) -> None:
        display_cards(self)
