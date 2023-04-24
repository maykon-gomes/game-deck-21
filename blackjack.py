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
        #{'value': value, 'suit': suit} = card
        random.shuffle(deck)
        return deck


    # Cria os usuaários
    # players será uma lista de dicionários c/ (mão e ponto)
    # hand será tmb sera uma lista de deck (dicionários)
    # esta função recebe o num_players, que por padrao é 1
    def create_players(self):
        players = []
        for i in range(self.num_players):
            players.append({'hand': [], 'score': 0})
            return players


    # Remover a primeira carta do deck
    def remove_first_card(self):
        self.deck.pop(0)


    # Dar as cartas
    # para cada player 2 cartas (entraga a 1ª / remove do deck)
    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                player['hand'].append(self.deck[0])
                self.remove_first_card()

    # Pontos da mão
    # non_aces=Soma das cartas + quantidade de aces
    # se os pontos + 10 forme <= 21 (soma + 10 pontos) ace valera 11
    def hand_points(self, hand):
        non_aces = [card['value'] for card in hand if card['value'] != 'Ace']
        aces = [card['value'] for card in hand if card['value'] == 'Ace']
        score = sum(non_aces) + len(aces)
        for ace in aces:
            if score + 10 <= 21:
                score += 10
                return score

    # jogada do usuario
    #
    def user_actions(self, player):
        while True:
            print('\n ############ Your Hand ############\n')
            print(f'Your cards {player["hand"]}, sum: {self.hand_points(player["hand"])}')
            print('\n\n############ Dealer Hand ############\n')
            print(f"Dealer's first card: {self.players[0]['hand'][0]}\n")
            action = input('1 - HIT\n2 - STAND\n')
            if action == '1':
                player['hand'].append(self.deck[0])
                self.remove_first_card()
                print(f'\nYour new card is {player["hand"][-1]}')
                if self.hand_points(player['hand']) > 21:
                    print(f'\nYour cards {player["hand"]}, sum: {self.hand_points(player["hand"])}')
                    print('\n\n############ Dealer Hand ############\n')
                    print(f"Dealer's hand: {self.players[0]['hand']}\n")
                    print('You Busted! Better luck next time')
                    return 'BUSTED'
                elif action == '2':
                    return 'STAND'

    def dealer_actions(self):
        while True:
            print('\n\n############ Dealer Hand ############\n')
            print(f"Dealer's hand: {self.players[0]['hand']}, sum: {self.hand_points(self.players[0]['hand'])}\n")
            if self.hand_points(self.players[0]['hand']) < 17:
                self.players[0]['hand'].append(self.deck[0])
                self.remove_first_card()
                print(f"\nDealer's new card is {self.players[0]['hand'][-1]}")
            elif self.hand_points(self.players[0]['hand']) > 21:
                print(f"\nDealer's hand: {self.players[0]['hand']}, sum: {self.hand_points(self.players[0]['hand'])}")
                print('Dealer Busted! You win')
                return 'DEALER BUSTED'
            else:
                print(f"\nDealer's hand: {self.players[0]['hand']}, sum: {self.hand_points(self.players[0]['hand'])}")
                return 'DEALER STAND'

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
                        print(f'Player {i} Loses!')
                    else:
                        print(f'Player {i} Ties!')

bj = Blackjack()
bj.deal_cards()
bj.user_actions()