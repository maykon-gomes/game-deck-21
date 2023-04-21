'''
fruits = ['apple', 'banana', 'cherry','orange', 'grape', 'straberry']

def op():
  while True:
    ac = int(input('option'))
    if ac == 1:
       
      fruits.remove(fruits[0])
      print(fruits)
    else:
    		break
    
    
print(fruits)
op()
'''
deck = [ 2, 3, 4, 5, 6, 7, 8, 9, 10]

deck_completo = deck * 4

print(deck_completo)