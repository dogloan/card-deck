"""
TO DO create a player class that can be used by the BlackJackDealer to
control rounds
at first just base them off dealer? first ai should just split doubles
third can double down below 9 or something
"""
import random

class Player:
    """ create a player who can hold a hand of cards and money
    TO DO create player behavior based on hands"""

    def __init__(self, money = 100):
        """ players will have a list of hands and an int of money
        hand 0 will be a list, hand 1 will only occur if they split """
        self.hand = {0: [], 1: False}
        """ money is set to 100 by default but Player can be called with a
        different amount """
        self.money = money
        """ this will let us keep track of players scores in blackjack """
        self.hand_value_blackjack = {}
        self.blackjack_score = 0
        self.blackjack_bust = False
        self.blackjack = False

class Deck:
    """ Deck will make decks for us, remember them, and have other
    card related functions """

    def __init__(self):
        """ create an empty list that will hold our cards """
        self.deck = []

    def deck_blackjack(self, decks = 1):
        """ build a deck of 52 cards with face, suit, and real value
        the face value will be used to detect aces and doubles,
        the real value will be used for determing score in blackjack
        repeat for decks amount, default is 1
        real values: (1 = 11) (2-10 = face value) (11-13 = 10)
        """
        self.deck.clear()
        for n in range(decks):
            """ create 52 cards for every decks function called with """
            for n in range(1,53):
                """ every 13 cards will have a face value of 1-13, a suit value,
                and a real value assigned in chunks of 13 """
                if n in range(14):
                    self.deck.append([n, "h", n])
                elif n in range(13,27):
                    self.deck.append([n - 13, "d", n - 13])
                elif n in range(26,40):
                    self.deck.append([n - 26, "c", n - 26])
                else:
                    self.deck.append([n - 39, "s", n - 39])
        """ set real values to match the face cards value in blackjack"""
        for n in self.deck:
            if n[2] >= 11:
                n[2] = 10
            elif n[0] == 1:
                n[2] = 11
        self.deck_shuffle()

    def deck_shuffle(self):
        random.shuffle(self.deck)

    def deal_topcard(self):
        """ pop will remove the last item in the list and give us its value
        this removes the card from self.deck to prevent doubles """
        card = self.deck.pop()
        """ we'll return the value of the card for the Dealer use later """
        return card

    def deal_random(self):
        """ pick a card at random with choice, remove it from the deck,
        return the value for the Dealer use later"""
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

class Dealer(Player):
    """ this class will manage the deck, players, turn rounds,
    all dealer activities """

    def __init__(self):
        """ dealer is a subclass of Player """
        super().__init__()
        """ self.deck will be an object of the Deck class """
        self.deck = Deck()
        """ self.players will be a dictionary of players """
        self.players = {}

    def set_table(self, player_amount = 1):
        """ add players to player list, prepare to deal
        default player_amount = 1 """
        for n in range(player_amount):
            self.players[n] = Player()

    def announce_players(self):
        """ return statement announcing how many players are at the table """
        player_amount = len(self.players)
        statement = f"There are {player_amount} players at the table."
        return statement

    def blackjack_initial_deal(self):
        """ deal the initial blackjack hands, giving cards to all players
        and the dealer. clear all hands first """
        self.hand[0].clear()
        for n in self.players:
            self.players[n].hand[0] = []
            self.players[n].hand[1] = False
        """ dealing round one """
        for n in self.players:
            player_card = self.deck.deal_topcard()
            self.players[n].hand[0].append(player_card)
        dealer_card = self.deck.deal_topcard()
        self.hand[0].append(dealer_card)
        """ dealing round two """
        for n in self.players:
            player_card = self.deck.deal_topcard()
            self.players[n].hand[0].append(player_card)
        dealer_card = self.deck.deal_topcard()
        self.hand[0].append(dealer_card)
        """ set scores for all players and whether they hit or busted """
        self.hand_value_blackjack = self.hand_counter(self.hand[0])
        for n in self.players:
            self.players[n].hand_value_blackjack = self.hand_counter(self.players[n].hand[0])

    def hand_counter(self, hand):
        """ we need to keep track of how many cards the hand has and what
        the total valaue of its real values are """
        score_count = 0
        card_count = 0
        """ we need ace check for if they bust on an ace value of 11 """
        ace_count = 0
        """ this is the information we'll ultimately return with all the information
        the computer will need about the hand """
        final_count = {"score": score_count,
                        "bust": False,
                        "blackjack": False,
                        "split":False}
        """ we're going to count  how many cards are in the hand
        # and add together the real values which is n[2] """
        for n in hand:
            card_count += 1
            score_count += n[2]
            if n[0] == 1:
                ace_count += 1
        """ check for two card blackjack
         card count of 2 let's us know it's their initial deal """
        if card_count == 2:
            """ let's see if they have doubles, that'll be good to know
            if the player wants to split so we'll set split to True """
            if hand[0][0] == hand[1][0]:
                final_count["split"] = True
            """ you need a score of 21 for blackjack """
            if score_count == 21:
                """ they made 21 in two cards, this is a blackjack """
                final_count["score"] = score_count
                final_count["bust"] = False
                final_count["blackjack"] = True
                return final_count
            elif score_count > 21:
                """ bust in two cards """
                final_count["score"] = score_count
                final_count["bust"] = True
                final_count["blackjack"] = False
                """ if they have aces and are busting, those will become
                 1s instead of 11s """
                while ace_count > 0 and score_count > 21:
                    ace_count -= 1
                    score_count -= 10
                    if score_count <= 21:
                        final_count["bust"] = False
                return final_count
            else:
                """ 21 or under """
                final_count["score"] = score_count
                final_count["bust"] = False
                final_count["blackjack"] = False
                return final_count
        elif score_count > 21:
            """ if they have aces and are busting, those will become
            1s instead of 11s """
            while ace_count > 0 and score_count > 21:
                ace_count -= 1
                score_count -= 10
                final_count["score"] = score_count
                final_count["bust"] = True
                final_count["blackjack"] = False
                return final_count
            """ over 21 thats a bust """
            final_count["score"] = score_count
            final_count["bust"] = True
            final_count["blackjack"] = False
            return final_count
        else:
            """ 21 or under """
            final_count["score"] = score_count
            final_count["bust"] = False
            final_count["blackjack"] = False
            return final_count
