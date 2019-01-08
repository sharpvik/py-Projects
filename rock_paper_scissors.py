from random import randint #this is a commend so the computer can choose a random number
print('rock = O')
print('paper = ___')
print('scrissors = >8')
print(' ')
player = input('rock(r), paper(p) or scrissors(s)? ')
if player == 'r':
    print('O vs ', end='')
elif player == 'p':
    print('___ vs ', end='')
elif player == 's':
    print('>8 vs ', end='' )
choice = randint(1,3)
while True :
    if choice == 1:
        print('O')
        if player == 'p':
            print('Player wins!')
            break
        elif player == 's':
            print('Computer wins!')
            break
        elif player == 'r':
            print('Again!')
            choice = randint(1, 3)
            player = input('rock(r), paper(p) or scrissors(s)? ')
        else:
            print("Wrong choice!")
            break
    if choice == 2:
        print('___')
        if player == 'p':
            print('Again!')
            player = input('rock(r), paper(p) or scrissors(s)? ')
            choice = randint(1, 3)
        elif player == 's':
            print('Player wins!')
            break
        elif player == 'r':
            print('Computer wins!')
            break
        else:
            print("Wrong choice!")
            break;
    if choice == 3:
        print('>8')
        if player == 'p':
            print('Computer wins')
            break
        elif player == 's':
            print('Again!')
            player = input('rock(r), paper(p) or scrissors(s)? ')
            choice = randint(1, 3)
        elif player == 'r':
            print('Player wins!')
            break
        else:
            print("Wrong choice!")
            break;
