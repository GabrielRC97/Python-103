import random

computer_wins = 0
user_wins = 0
rounds = 1

def choose_option():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Elija piedra, papel o tijera => ').lower()
  computer_option = random.choice(options)

  if not user_option in options:
    return None, None

  print('user_option => ' + user_option)
  print('computer_option => ' + computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option is None:
    print('esa opcion no es valida, vuelva a intentarlo')
  elif user_option == computer_option:
    print('Es un empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra le gana a tijera')
      print('Gana el user')
      user_wins += 1
    else:
      print('papel le gana a la piedra')
      print('Gana la computadora')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera le gana a papel')
      print('Gana el user')
      user_wins += 1
    else:
      print('piedra le gana a la tijera')
      print('Gana la computadora')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel le gana a piedra')
      print('Gana el user')
      user_wins += 1
    else:
      print('tijera le gana a papel')
      print('Gana la computadora')
      computer_wins += 1

  return user_wins, computer_wins

def check_winner(computer_wins, user_wins, rounds, user_option):
  if computer_wins == user_wins +2:
    print('Gano la computadora')
    return None  
  if user_wins == computer_wins +2:
    print('Gano el usuario')
    return None
  if user_option is None:
    return rounds
  rounds += 1 
  return rounds

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while rounds is not None:

    print('')
    print ('*' * 10)
    print ('ROUND', rounds)
    print ('*' * 10)
    print('')

    user_option, computer_option = choose_option()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    print('')
    print('Computadora:', computer_wins)
    print('usuario:', user_wins)

    rounds = check_winner(computer_wins,user_wins,rounds, user_option)

run_game()