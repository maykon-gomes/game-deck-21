def puxar_carta(deck):
	deck.remove(deck[0])

def dar_cartas(jogadores, deck):
	jog = jogadores * 2 #dois = duas cartas
	
	while jog > 0:
		puxar_carta(deck)
		jog -= 1

def pontuation(hand1, hand2):
	print('\n ############ Cartas do usuário ############\n')
	print(f'Suas cartas {hand1}, somao: {sum(hand1)}')
	print('\n\n############ Cartas do Computador ############\n')
	print(f'IA cartas {hand2}, somao: {sum(hand2)}\n')

def resultado(hand1, hand2):
	pontuation(hand1, hand2)
	if sum(hand1) > 21 and sum(hand2) <= 21:
		print('PC ganhou!')
	elif sum(hand2) > 21 and sum(hand1) <=21:
		print('Usuário ganhou!')
	elif sum(hand1) > sum(hand2) and sum(hand1) <= 21:
		print('Usuário ganhou!')
	elif sum(hand1) == sum(hand2):
		print('Empate!')
	else:
		print('PC ganhou!')

def action_user(hand1, hand2, deck):
	while True:
		if sum(hand1) <= 21:
			action = int(input('1 - HIT\n2 - STAND\n'))
			
			if action == 1:
				hand1.append(deck[0])
				puxar_carta(deck)
				action_pc(hand2, deck)
				pontuation(hand1, hand2)
				if sum(hand1) > 21 or sum(hand2) > 21:
					resultado(hand1, hand2)
					break
			elif action == 2:
				if sum(hand2) < sum(hand1):
					action_pc(hand2, deck)
					pontuation(hand1, hand2)
					break
				elif sum(hand1) == sum(hand2):
					resultado(hand1, hand2)
					action_pc(hand2, deck)
					break
				elif sum(hand2) > sum(hand1) and sum(hand2) <= 21:
					pontuation(hand1, hand2)
					action_user(hand1, hand2, deck)
					continue
				elif sum(hand1) > 21 or sum(hand2) > 21:
					resultado(hand1, hand2)
					break
				else:
					print('Parei')
					action_pc(hand2, deck)
					pontuation(hand1, hand2)
					break
		else:
			resultado()
			break

def action_pc(hand2, deck):
	if sum(hand2) < 18:
		hand2.append(deck[0])
		puxar_carta(deck)
		print('Puxar carta')
		
	else:

		print('Parei')

def jogada(hand1, hand2, deck):
	action_user(hand1, hand2, deck)
	action_pc(hand2, deck)
