import random

class BlackJackDealer:
    def __init__(self):
        self.deck = []
        self.dealer_hand = []
        self.player_hand = {}

    """ build a deck of 52 cards with face, suit, and real value
    the face value will be used to detect aces and doubles, the suit is
    useless but hey, the real value will be used for determing score
    (1 = 11/1) (2-10 = face value) (11-13 = 10)
    """
    def deck_builder(self, decks = 1):
        # deck is the list that will hold our cards
        # if called with an integer we'll add that many decks, otherwise
        # it's single deck blackjack
        for n in range(decks):
            for n in range(1,53):
                # every 13 cards will have a face value of 1-13, a suit value,
                # and a real value
                # we'll assign this for every 13 cards
                if n in range(14):
                    # assign value for first 13 cards
                    self.deck.append([n, "h", n])
                elif n in range(13,27):
                    # assign value for next 13
                    self.deck.append([n - 13, "d", n - 13])
                elif n in range(26,40):
                    # assign value for next 13
                    self.deck.append([n - 26, "c", n - 26])
                else:
                    # assign value for next 13
                    self.deck.append([n - 39, "s", n - 39])
        # make all real values 10 or less since that's blackjack max
        for n in self.deck:
            if n[2] >= 11:
                n[2] = 10
            elif n[0] == 1:
                n[2] = 11
        random.shuffle(self.deck)

    """ set the board with the initial deal before individual deals
    this function can take an integer input to increase the amount of
    players sitting at the table (dealt to)
    """
    def deal_initial(self, players = 1):
        # reset the player and dealer hands for a new initial deal
        self.player_hand.clear()
        self.dealer_hand.clear()
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

    """ this function will deal to individual players unlike deal_initial
    it will be given a hand and and append a card from the deck to it
    """
    def deal_individual(self,hand):
        card = self.deck.pop()
        hand.append(card)
    """
    add all the face values together for a total
    give back the entire dictionary of pertinant information in a
    blackjack deal
    TO DO if it's over 25 but an ace they need the other option than 11
    """
    def hand_counter(self, hand):
        score_count = 0
        card_count = 0
        # we need ace check for if they bust on an ace value of 11
        ace_count = 0
        final_count = {"score": score_count,
                        "bust": False,
                        "blackjack": False,
                        "split":False}
        # we're going to count  how many cards are in the hand
        # and add together the real values which is n[2]
        for n in hand:
            card_count += 1
            score_count += n[2]
            if n[0] == 1:
                ace_count += 1
        # check for two card blackjack
        # card count of 2 let's us know it's their initial deal
        if card_count == 2:
            # let's see if they have doubles, that'll be good to know
            # if the player wants to split so we'll set split to True
            if hand[0][0] == hand[1][0]:
                final_count["split"] = True
            # you need a score of 21 for blackjack
            if score_count == 21:
                # they made 21 in two cards, this is a blackjack
                final_count["score"] = score_count
                final_count["bust"] = False
                final_count["blackjack"] = True
                return final_count
            elif score_count > 21:
                # bust in two cards
                final_count["score"] = score_count
                final_count["bust"] = True
                final_count["blackjack"] = False
                # if they have aces and are busting, those will become
                # 1s instead of 11s
                while ace_count > 0 and score_count > 21:
                    ace_count -= 1
                    score_count -= 10
                    if score_count <= 21:
                        final_count["bust"] = False
                        print("saved by an ace")
                return final_count
            else:
                # 21 or under
                final_count["score"] = score_count
                final_count["bust"] = False
                final_count["blackjack"] = False
                return final_count
        elif score_count > 21:
            # if they have aces and are busting, those will become
            # 1s instead of 11s
            while ace_count > 0 and score_count > 21:
                ace_count -= 1
                score_count -= 10
                final_count["score"] = score_count
                final_count["bust"] = True
                final_count["blackjack"] = False
                return final_count
            # over 21 thats a bust
            final_count["score"] = score_count
            final_count["bust"] = True
            final_count["blackjack"] = False
            return final_count
        else:
            #  21 or under
            final_count["score"] = score_count
            final_count["bust"] = False
            final_count["blackjack"] = False
            return final_count

""" test instructions """
dealer = BlackJackDealer()
dealer.deck_builder()
dealer.deal_initial(4)
print("dealer hand:")
print(dealer.dealer_hand)
print("Dealer has a ", dealer.hand_counter(dealer.dealer_hand))
print()
print("player hands:")
for player in dealer.player_hand:
    print("Player ", player, " has: ", dealer.player_hand[player])
for player in dealer.player_hand:
    print("Player ", player, " has: ", dealer.hand_counter(dealer.player_hand[player]))
print()
print("deal 1 rounds then reveal:")
for n in range(1):
    for player in dealer.player_hand:
        dealer.deal_individual(dealer.player_hand[player])
print()
print("player hands:")
for player in dealer.player_hand:
    print("Player ", player, " has: ", dealer.player_hand[player])
for player in dealer.player_hand:
    print("Player ", player, " has: ", dealer.hand_counter(dealer.player_hand[player]))

print("dealer hand:")
print(dealer.dealer_hand)
dealer_value = dealer.hand_counter(dealer.dealer_hand)["score"]
print("Dealer has a ", dealer_value)
print()
print("Dealer is holding a ", dealer_value)
while dealer_value <= 16:
    print("Dealer draws.")
    dealer.deal_individual(dealer.dealer_hand)
    dealer_value = dealer.hand_counter(dealer.dealer_hand)["score"]
    if dealer_value > 21:
        print("dealer bust")
    print("Dealer is holding:")
    print(dealer_value)
    print()
print()
print("Dealer has a ", dealer_value)
print()
print("Remaining deck:")
print(dealer.deck)
