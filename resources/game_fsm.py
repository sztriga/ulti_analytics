from resources.deck import Deck
from resources.hand import Hand
from resources.stock import Stock


class GameFSM:
    def __init__(self):
        self.state = 'bidding'  # Initial state
        self.hands = []
        self.stock = Stock()
        self.pass_counter = 0  # Counts consecutive passes

    def start_bidding(self):
        print("Starting the Bidding phase...")

        # Initialize objects
        deck = Deck()
        self.hands = [Hand("Jimmy"), Hand("Brian"), Hand("Mike")]
        dealt_cards = deck.deal()

        # Deal cards to hands
        for i, hand in enumerate(self.hands):
            hand.pickup_cards(cards=dealt_cards[i])

        self.bidding_phase()

    def bidding_phase(self):
        # Hand 1 must put down stock first
        print(f"\n{self.hands[0].name}'s turn to put down two cards into the stock.")
        self.hands[0].show()
        index1 = int(input("Choose the first card index to put down (1-12): "))
        index2 = int(input("Choose the second card index to put down (1-12): "))
        self.hands[0].put_down_stock(index1 - 1 , index2 - 1, self.stock)

        current_player = 1  # Now it's Hand 2's turn to make decisions

        while self.state == "bidding":
            print(f"\nCurrent Player: {self.hands[current_player].name}'s turn.")
            self.hands[current_player].show()
            decision = input("Enter 'pass' to pass or 'pickup' to pick up the stock: ").strip().lower()

            if decision == "pickup" and self.stock.cards:
                # Player picks up the stock
                self.hands[current_player].pickup_stock(self.stock)
                print(f"{self.hands[current_player].name} picks up the stock.")
                self.hands[current_player].show()

                # Player must put down new stock
                index1 = int(input("Choose the first card index to put down (1, 2, 3...): "))
                index2 = int(input("Choose the second card index to put down (1, 2, 3...): "))
                self.hands[current_player].put_down_stock(index1 - 1, index2 - 1, self.stock)

                # Reset pass counter after stock pickup
                self.pass_counter = 0

            elif decision == 'pass':
                print(f"{self.hands[current_player].name} passes.")
                self.pass_counter += 1

                # Check for three consecutive passes
                if self.pass_counter >= 3:
                    print("Three consecutive passes! Transitioning to PLAY phase...")
                    self.state = 'play'
                    break

            # Move to the next player
            current_player = (current_player + 1) % 3

    def start_play_phase(self):
        print("\nTransitioning to the Play phase...")
        # Implement the play phase here
 