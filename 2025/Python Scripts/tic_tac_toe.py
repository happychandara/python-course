import random as rd
import time


# Creating grid
grid = list('         ')

# Winning combinations
winning_combos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]


# Playing turn function
def play(player):
    '''
    Player select cell in which they want to add a symbol.
    Returns True if player won, False otherwise
    '''
    # Player chooses an empty cell
    while True:
        n = int(input(f'\nEnter cell for {player} : '))
        if not n in range(1,10) or grid[n-1] != ' ':
            print('\nPlease pick an available cell !')
        else:
            grid[n-1] = player
            break

    # Printing grid
    print('\n', ' | '.join(grid[:3]))
    print('---+---+---')
    print('',' | '.join(grid[3:6]))
    print('---+---+---')
    print('',' | '.join(grid[6:]))

    # Check if a winning combo is obtained
    for combo in winning_combos:
        if all(grid[cell] == player for cell in combo):
            return True
    return False

# Bot playing turn function
def botplay():
    '''
    Bot selects cell randomly among those that are available
    Return True if bot won, False otherwise
    '''
    print('\nBot is thinking...')
    time.sleep(1.5)

    # Bot chooses a random available cell
    available = [i for i in range(9) if grid[i] == ' ']
    k = rd.choice(available)
    grid[k] = 'O'

    # Printing grid
    print('\n', ' | '.join(grid[:3]))
    print('---+---+---')
    print('',' | '.join(grid[3:6]))
    print('---+---+---')
    print('',' | '.join(grid[6:]))

    # Check if a winning combo is obtained
    for combo in winning_combos:
        if all(grid[cell] == player for cell in combo):
            return True
    return False


# Game settings
player1 = 'X'
player2 = 'O'
player = player1


# Opening screen
print('\n⋆⭒˚. (っ◔ ◡ ◔ )っ ˚⭒⋆')
print('╔═══════════════════╗')
print('║    𝙏𝙞𝙘-𝙏𝙖𝙘-𝙏𝙤𝙚    ║')
print('╚═══════════════════╝')
print(' [1] Single Player')
print(' [2] Two Players')
mode = int(input('\nChoose your mode : '))

# Printing empty grid
print('\n', ' | '.join(list('123')))
print('---+---+---')
print('',' | '.join(list('456')))
print('---+---+---')
print('',' | '.join(list('789')))


# Single player gameplay
if mode == 1:
    for i in range(9):
        if player == player1:
            won = play(player)
        else:
            won = botplay()

        if won and player == player1:
            print('\nPlayer wins !')
            break

        if won and player == player2:
            print('\nBot wins !')
            break

        player = player1 if player == player2 else player2

        if i == 8:
            print('\nIt\'s a draw !')


# 2 players gameplay
if mode == 2:
    for i in range(9):
        won = play(player)

        if won:
            print('\nPlayer', player, 'wins !')
            break

        player = player1 if player == player2 else player2

        if i == 8:
            print('\nIt\'s a draw !')