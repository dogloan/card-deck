import random

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
        self.players = players

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
    def card_puller(self, players = 1, cards = 1):

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
