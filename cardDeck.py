import random


"""
TO DO seperate pulling a card and adding cards to hands into seperate functions
TO DO seperate deck and dealer functions
TO DO currently the number of players dealt to card_puller can't exceed player amount
TO DO given to CardDeck
"""

class CardDeck:
# the CardDeck class will be used to create and track the deck, deal and remember
# cards, and basically do any other card related function or variable tracking

    # every instance of this class will have a deck list
    # can call CardDeck with a specific number of players otherwise default 1
    def __init__(self, players = 1):

        # create list variables to contain and track all deck, hand, and card information
        self.deck = []
        # self.hand will be a list of lists, each list being a players hand containing
        # a list of their cards
        self.hand = []

        # create a hand for each player and add it to the master list of hands
        for n in range(players):
            self.hand.append([])

    # the purpose of the deck_builder function is to return a list containing
    # a standard 52 deck of playing cards
    # jokers can be added to the deck if function is called with a value,
    # otherwise the default amount of jokers is 0
    def deck_builder(self, jokers = 0):

        # deck is the list that will hold our cards
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

        # add jokers if deck_builder was called with a joker amount
        # otherwise don't
        if jokers > 0:
            for n in range(jokers):
                self.deck.append([0, "j"])

    # the purpose of the card puller is to pull a card from the deck,
    # add it to the hand, and remove the pulled card from the remaining deck
    # so that it cannot be pulled again until the deck is reset
    def card_puller(self, cards, players = 1):

        # card_puller will pull as many cards as prompted or pull just one
        # if not called with an integer
        # for as many players as prompted or else for just one player if not
        # called with an integer
        # (dealing western style, one card to each player, then around again)
        for n in range(cards):
            for n in range(players):
                # pick a card any card
                card = random.choice(self.deck)
                # add chosen card to hand
                self.hand[n].append(card)
                # remove chosen card from decks
                self.deck.remove(card)

    # shuffle the deck, not to be confused with reseting it
    def deck_shuffler(self):
        random.shuffle(self.deck)

    # translator the card information into normal english
    def card_translator(self, card):
        # this will be the new values
        face_value = ""
        suit_value = ""

        # lets figure out the face value of the card
        if card[0] in range(10):
            face_value = str(card[0])
        elif card[0] == 10:
            face_value = "jack"
        elif card[0] == 11:
            face_value = "queen"
        elif card[0] == 12:
            face_value = "king"
        else:
            face_value = "ace"

        # lets figure out the suit of the card
        if card[1] == "h":
            suit_value = "hearts"
        elif card[1] == "d":
            suit_value = "diamonds"
        elif card[1] == "c":
            suit_value = "clubs"
        else:
            suit_value = "spades"

        # make a new string of our new card and return that value
        translated_card = "".join([face_value, " of ", suit_value])
        return translated_card


    # print hands
    """
    TO DO see_hands is still under construction
    """
    def see_hands(self):
        # everytime we count out a new players hand we'll add them to our
        # player count
        player_count = 0

        # read out hands and count players
        for n in self.hand:
            player_count += 1
            player_hand = n
            player_statement = "".join(["Player ", str(player_count), " has:"])
            print(player_statement)
            player_cards = 0
            while player_cards < len(player_hand):
                card = player_hand[player_cards]
                print(self.card_translator(card))
                player_cards += 1
                
