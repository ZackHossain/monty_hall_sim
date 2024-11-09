# monty_hall_sim.py

import random
from tabulate import tabulate
import time

correct_key = 'correct'
wrong_key = 'wrong'
stay = {
    'correct': 0,
    'wrong': 0,
    'iterations': 0
}
swap = {
    'correct': 0,
    'wrong': 0,
    'iterations': 0
}

# simulates a game of the Monty Hall Problem
def simulate(action):
    options = ['1','2','3']
    doors = get_doors(options)
    
    choice = random.choice(options)
    options.remove(choice)
    
    revealed = reveal_one(doors, options)
    options.remove(revealed)
    
    if (action == 'stay'):
        outcome = is_correct(doors, choice)
    else:
        choice = options[0]
        outcome = is_correct(doors, choice)
    
    return outcome

# randomly assigns the car to a door
# returns a dict of doors
def get_doors(options):
    doors = {
        '1': 'goat',
        '2': 'goat',
        '3': 'goat'
    }
    correct = random.choice(options)
    doors[correct] = 'car'
    return doors

# returns the doors dict key for one of the goats
def reveal_one(doors, options):
    for option in options:
        if doors[option] == 'goat':
            return option

# checks if the simulation has found the car
def is_correct(doors, choice):
    if (doors[choice] == 'car'):
        return correct_key
    else:
        return wrong_key

# Gets validated user input for number of iterations
def get_iterations(msg):
    while True:
        try:
            num = int(input(msg))
            if num > 0:
                return num
            msg = 'Please enter a positive integer: '
            continue
        except Exception:
            msg = 'Please enter a positive integer: '
            continue

# prints simulation stats in a table
def print_stats(stats, title):
    correct = stats[correct_key]
    wrong = stats[wrong_key]
    
    if wrong == 0:
        correct_percent = 100;
    else:
        correct_percent = correct * 100 / wrong
    
    print(title, ' Results:')
    print(tabulate([
        ['W/L Ratio', f'{correct}:{wrong}'],
        ['W/L %', f'{correct_percent:.2f}%'],
        ['Win Rate (%)', f'{(100 * correct / stats['iterations']):.2f}%']
    ]), '\n')

# main function
if __name__ == '__main__':
    num = get_iterations('How many iterations? ')
    stay['iterations'] = num
    swap['iterations'] = num
    
    start = time.time()
    
    for x in range(num):
        # print('ITERATION ', x)
        res = simulate('stay')
        stay[res] += 1
        res = simulate('swap')
        swap[res] += 1
        
    end = time.time()
    
    print(f'\nTime Elapsed: {end - start}s\n')
    print_stats(stay, 'Stay')
    print_stats(swap, 'Swap')
    