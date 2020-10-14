import random
choice = 'j':
while choice == 'j':
  roll = random.randint(1, 6)
  print(f'du slår {roll:1}')
  choice =input('vill du slå en tärning[j/n]: ').lower()[0]
  print('hej då')  
