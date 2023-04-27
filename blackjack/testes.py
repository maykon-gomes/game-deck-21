
import random

class Blackjackkk:
    def __init__(self):
        self.players = self.create_players()
        self.deck = self.create_deck()

    def create_deck(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
        deck = [{'value': value, 'suit': suit} for suit in suits for value in values]
        #deck[x] = card  => {'value': value, 'suit': suit}
        random.shuffle(deck)
        return deck

    def create_players(self):
        players = []
        for i in range(2):
            i = str(i+1)
            players.append({'nick':'player'+i,'hand': [], 'score': 0, 'coins': 500})
        return players

    def remove_first_card(self):
        self.deck.pop(0)

    def deal_cards(self):
        for i in range(2):
            for player in range(len(self.players)):
                self.players[player]['hand'].append(self.deck[0])
                self.remove_first_card()
        #IMPRIMINDO PARA VISUALIZAÇÃO DOS TESTES
        hand = [self.players[i] for i in range(len(self.players))]
        print(hand)

    def point(self):
        player_points = []
        for player in range(len(self.players)):
            hand_score = 0
            for card in range(len(self.players[player]['hand'])):
                value = self.players[player]['hand'][card]['value']
                if type(value) == str:
                    value = 10
                else:
                    pass                           
                hand_score += value
                 

            player_points.append(hand_score)
        print(player_points)

        #total = [self.players[player]['hand'][0]['value'] for player in range(len(self.players)) ]
        #print (total)

bj = Blackjackkk()
bj.create_deck()
bj.create_players()
bj.deal_cards()
bj.point()

