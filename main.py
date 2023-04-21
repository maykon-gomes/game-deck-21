#Considere um jogo de cartas em que o objetivo é obter a maior pontuação possível sem ultrapassar 21. 

#As cartas têm valores de 1 a 10 e as figuras (Valete, Rainha e Rei) valem 10 pontos cada. 
#O Ás pode valer 1 ou 11 pontos, dependendo da situação. se pontos<=10 : às =11 senao as = 1

#Você deve implementar um programa que simule esse jogo e permita que o jogador faça suas jogadas. 
#As regras do jogo são as seguintes:

############# REGRAS ###################
#Cada jogador começa com duas cartas.
#O jogador pode pedir mais cartas (hit) ou parar (stand).
#Se a soma das cartas do jogador ultrapassar 21, ele perde automaticamente.
#Se o jogador parar, o computador joga e pede mais cartas até somar pelo menos 17 pontos. (aki entra estatistic pandas)
#Se o computador ultrapassar 21, o jogador ganha automaticamente.
#Se o jogador e o computador tiverem pontuações iguais, é considerado empate.

#==================================================================#

from random import shuffle
import functions as ft

#Inicializar o jogo com as cartas embaralhadas.
ace = 1
jack = 10
queen = 10
king = 10

#BARALHO  VALORES POSSIVEIS #### PARA NAIPES ==> MATRIZ
deck = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]
deck_full = deck * 4

#EMBARALHAR
shuffle(deck_full)

#jogadores = int(input('Quantidade de jogadores:'))
jogadores = 2

#DAR AS CARTAS
#Distribuir as cartas para o jogador e para o computador.
hand1 = [deck_full[0], deck_full[2]]
hand2 = [deck_full[1], deck_full[3]]

ft.dar_cartas(jogadores,deck_full)

#Exibir as cartas do jogador e a carta do computador que está virada para baixo.

ft.pontuation(hand1, hand2)

#Permitir que o jogador faça suas jogadas.
#Exibir a pontuação do jogador e do computador após cada jogada.
#Exibir o resultado final do jogo (quem ganhou ou se foi empate).

ft.jogada(hand1, hand2, deck_full)