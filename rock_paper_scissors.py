import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
OPTIONS = (ROCK, PAPER, SCISSORS)

# who bets who
RULES = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

# traceback from first letter to whole word
TRACE = {
    ROCK: 'rock',
    PAPER: 'paper',
    SCISSORS: 'scissors',
}


def who_wins(usr, cpu):
    print(f'\nUser chose: {TRACE[usr]}\nComputer chose: {TRACE[cpu]}')

    if usr == cpu:
        return 'It is a tie.'

    if RULES[usr] == cpu:
        return 'Human wins!'

    return 'Computer wins!'


def play():
    # get user to choose something appropriate
    usr = None
    while not usr:
        choice = input('Rock(r), Paper(p) or Scrissors(s)? ').strip()[0].lower()
        usr = choice if choice in OPTIONS else None

    # cpu to choose
    cpu = random.choice(OPTIONS)

    print( who_wins(usr, cpu) + '\n' )


if __name__ == '__main__':
    try:
        while True:
            play()

    except KeyboardInterrupt:
        print('\nThanks for playing with me!')
