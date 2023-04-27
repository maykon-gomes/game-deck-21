import random

class Blackjack:
    # Método construtor: o Objeto Blackjack possui (num_players, deck, players)
    # self nos permite usar os atributos/métodos do no obj Blackjack
    def __init__(self, num_players=1):
        self.num_players = num_players
        self.deck = self.create_deck()
        self.players = self.create_players()


    # Cria o baralho
    # Um dicionário com (valores de 2 a 11 + Desenhos) , Espadas, Copas , Ouros, Pals.
    # Usa-se o loop for para criar o deck.
    # embaralha
    def create_deck(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
        deck = [{'value': value, 'suit': suit} for suit in suits for value in values]
        #deck[x] = card  => {'value': value, 'suit': suit}
        random.shuffle(deck)
        return deck

        #deck=[{'value':2, 'suit':'spades'}, {'value':7, 'suit':'clubs'}...n]
        #deck=[0]['value'] => 2

    # Cria os usuaários
    # players será uma lista de dicionários c/ (mão e ponto)
    # hand será tmb sera uma lista de deck (dicionários)
    # esta função recebe o num_players, que por padrao é 1
    def create_players(self):
        players = []
        for i in range(self.num_players):
            i = str(i+1)
            players.append({'nick':'player'+i,'hand': [], 'score': 0, 'coins': 500})
        return players

        #players[0] = [{'nick':player1, 'hand':{'value':2, 'suit':'spades'}, {'value':7, 'suit':'clubs'}, 'coins': 500}]
        #players[0]['nick'] = player1
        #players[0]['hand'] = {'value':2, 'suit':'spades'}, {'value':7, 'suit':'clubs'}
        #players[0]['coins'] = 500


    # Remover a primeira carta do deck
    def remove_first_card(self):
        self.deck.pop(0)


    # Dar as cartas
    # para cada player 2 cartas (entraga a 1ª / remove do deck)
    def deal_cards(self):
        for i in range(2):
            for player in range(len(self.players)):
                self.players[player]['hand'].append(self.deck[0])
                self.remove_first_card()

    # Pontos da mão
    # non_aces=Soma das cartas + quantidade de aces
    # se os pontos + 10 forme <= 21 (soma + 10 pontos) ace valera 11
    def hand_points(self):
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

        '''
        non_aces = [card['value'] for card in hand if card['value'] != 'Ace']
        aces = [card['value'] for card in hand if card['value'] == 'Ace']
        score = sum(non_aces) + len(aces)
        for ace in aces:
            if score + 10 <= 21:
                score += 10
                return score
        '''
    def play_game(self):
        self.deal_cards()
        for i in range(1, len(self.players)):
            while self.user_actions(self.players[i]) != 'STAND':
                pass
            dealer_result = self.dealer_actions()
            for i in range(1, len(self.players)):
                if self.hand_points(self.players[i]['hand']) > 21:
                    continue
                elif dealer_result == 'DEALER BUSTED':
                    print(f'Player {i} Wins!')
                elif self.hand_points(self.players[i]['hand']) > self.hand_points(self.players[0]['hand']):
                    print(f'Player {i} Wins!')
                elif self.hand_points(self.players[i]['hand']) < self.hand_points(self.players[0]['hand']):
                    print(f'Dealer Wins! Player {i} lost')
                else:
                    print(f'Player {i} and dealer tie')
            print(f"\n\nDealer's final hand: {self.players[0]['hand']}, sum: {self.hand_points(self.players[0]['hand'])}")
            for i in range(1, len(self.players)):
                print(f'Player {i} hand: {self.players[i]["hand"]}, sum: {self.hand_points(self.players[i]["hand"])}')

    if __name__ == 'main':
        num_players = int(input('Enter number of players (default=1): '))
        bj = Blackjack(num_players)
        bj.play_game()