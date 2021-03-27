import enum
import random


class Suit(enum.Enum):
    SPADES = "Spades"
    CLUBS = "Clubs"
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"


class Value(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit: Suit):
        if suit not in Suit:
            raise ValueError(f"Invalid suit. Must be one of {Suit.keys()}")
        self._suit = suit

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Value):
        if value not in Value:
            raise ValueError(f"Invalid Value. Must be one of {Value.keys()}")
        self._value = value

    def __repr__(self):
        return f"{self.value.name.title()} of {self.suit.value}"


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in Suit for v in Value]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    @property
    def value(self):
        value = 0
        has_ace = False

        for card in self.cards:
            value += card.value.value
            if not has_ace:
                has_ace = card.value == Value.ACE

        if has_ace and value > 21:
            value -= 10
        return value

    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.value)


class Game:
    def __init__(self):
        pass

    def play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for _ in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is: ")
            self.dealer_hand.display()

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()

                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack
                    )
                    continue

                choice = input("PLease chose [Hit / stand] ").lower()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("PLease chose [Hit / stand] or (h/s)").lower()
                if choice in ["hit", "h"]:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost !")
                        game_over = True

                else:
                    player_hand_value = self.player_hand.value
                    dealer_hand_value = self.dealer_hand.value

                    print("Final Results")
                    print(" Your hands:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You Win!")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")

                    game_over = True

            again = input("Play Again?")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.value > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.value == 21:
            player = True
        if self.dealer_hand.value == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("Player has blackjack! Player wins!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")


if __name__ == "__main__":
    g = Game()
    g.play()
