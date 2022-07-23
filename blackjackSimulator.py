import random

class BlackJackDealer:
    def __init__(self):
        self.deck = []
        self.dealer_hand = []
        self.player_hand = {}
    def deck_builder(self, decks = 1):
        # deck is the list that will hold our cards
        # if called with an integer we'll add that many decks, otherwise
        # it's single deck blackjack
        for n in range(decks):
            for n in range(1,53):
                # every 13 cards will have a face value of 1-13 and a suit
                # we'll assign this for every 13 cards
                if n in range(14):
                    # assign value for first 13 cards
                    self.deck.append([int(n), "h"])
                elif n in range(13,27):
                    # assign value for next 13
                    self.deck.append([(int(n)-13), "d"])
                elif n in range(26,40):
                    # assign value for next 13
                    self.deck.append([(int(n)-26), "c"])
                else:
                    # assign value for next 13
                    self.deck.append([(int(n)-39), "s"])
        random.shuffle(self.deck)

    # set the board with the initial deal before individual deals
    def initial_deal(self, players = 1):
        # first card for all players
        for n in range(players):
            player_number = n + 1
            card = self.deck.pop()
            self.player_hand[player_number] = []
            self.player_hand[player_number].append(card)
        # first card for dealer
        card = self.deck.pop()
        self.dealer_hand.append(card)
        # second card for all players (face down)
        for n in range(players):
            player_number = n + 1
            card = self.deck.pop()
            self.player_hand[player_number].append(card)
        # second card for dealer (face up)
        card = self.deck.pop()
        self.dealer_hand.append(card)

    # add all the face values together for a total
    def hand_counter(self, hand):
        running_count = 0
        for n in hand:
            running_count += n[0]
        return running_count
