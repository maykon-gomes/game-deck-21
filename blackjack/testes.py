
import random

class Blackjackkk:
    def __init__(self, num_players=1):
        self.num_players = num_players
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
        for i in range(self.num_players):
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

    # pontos do Ace são variaveis 1 ou 11
    def check_ace(self):
        if len(self.aces) > 0:
                for play in self.aces:
                    indice = self.aces[len(play)-1] #aces[0]
                    i = int(indice['Ace'][-1:]) - 1 #0
                    ace = self.player_points[i]
                    if ace + 10 <= 21:
                        ace += 10
                        self.player_points[i] = ace
                        

    def point(self):
        self.player_points = [] #lista de pontos
        self.aces = []
        for player in range(len(self.players)):
            if True:
                hand_score = 0
                for card in range(len(self.players[player]['hand'])):
                    value = self.players[player]['hand'][card]['value']
                    if type(value) == str and value != 'Ace':
                        value = 10
                    elif value == 'Ace':
                        value = 1
                        self.aces.append({'Ace': self.players[player]['nick']})

                    hand_score += value
                     
                self.player_points.append(hand_score)

        self.check_ace()
        print(self.player_points)
        print(self.aces)
        
        #total = [self.players[player]['hand'][0]['value'] for player in range(len(self.players)) ]
        #print (total)

    def user_action(self):
        for player in self.players:
            action = int(input("1 - HINT \n2 - STAND\n"))
            if action == 1:
                self.players[player]['hand'].append(self.deck[0]) ###no dict
                self.remove_first_card()
                print(f'\nYour new card is :{self.players[player]["hand"][-1]}')
                if self.point(self.players[player]["hand"]) > 21: ####ERROR retornando dicionário
                    print(f'\nYour cards {player["hand"]}, sum: {self.hand_points(player["hand"])}')
                    print('\n\n############ Dealer Hand ############\n')
                    print(f"Dealer's hand: {self.players[0]['hand']}\n")
                    print('You Busted! Better luck next time')
                    return 'BUSTED'
            elif action == '2':
                return 'STAND'


bj = Blackjackkk(4)
bj.create_deck()
bj.create_players()
bj.deal_cards()
bj.user_action()
bj.point()

