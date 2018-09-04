"""
Program that tests the monty hall problem.
"""

from __future__ import division
import random
import time

#
def pick_one_door(runtime):
    # defines default values
    #win_doors = []
    choices = []
    wins = []
    then = time.time()
    now = 0
    while now <= runtime:
        now = time.time()-then
        # choose winning door
        winning_door = random.choice('abc')
        #win_doors.append(winning_door)
        # contestant chooses door
        choice = random.choice('abc')
        choices.append(choice)
        # determines if the contestant chose the right door
        if choice == winning_door:
            # tally the win and record the choice
            wins.append(choice)
    return wins, choices

def pick_two_doors(runtime):
    win_doors = []
    first_choices = []
    choices = []
    wins = []
    three_doors = ['a', 'b', 'c']
    then = time.time()
    now = 0
    while now <= runtime:
        now = time.time()-then
        # copies the three door list
        two_doors = three_doors[:]
        winning_door = random.choice('abc')
        win_doors.append(winning_door)
        # determines which two doors have goats behind them
        if winning_door == 'a':
            goat1 = 'b'
            goat2 = 'c'
        elif winning_door == 'b':
            goat1 = 'c'
            goat2 = 'a'
        else:
            goat1 = 'a'
            goat2 = 'b'
        # picks random door, then discards answer by removing
        # from the list, searches the remaining two elements
        choice = random.choice('abc')
        first_choices.append(choice)
        if choice == goat1:
            first_pick = choice
            show_goat = goat2
            # picker wont pick the shown goat and has to
            # change doors
            two_doors.remove(show_goat)
            two_doors.remove(first_pick)
            # picks the only element left in the array
            modified_choice = two_doors[-1]
            choices.append(modified_choice)
        elif choice == goat2:
            first_pick = choice
            show_goat = goat1
            two_doors.remove(show_goat)
            two_doors.remove(first_pick)
            modified_choice = two_doors[-1]
            choices.append(modified_choice)
        elif choice == winning_door:
            first_pick = winning_door
            show_goat = goat1
            two_doors.remove(show_goat)
            two_doors.remove(first_pick)
            modified_choice = two_doors[-1]
            choices.append(modified_choice)
        if modified_choice == winning_door:
            wins.append(choices)
    return wins, choices

def do_maths(wins, choices, type):
    # defines default values
    a_picked = choices.count('a')
    b_picked = choices.count('b')
    c_picked = choices.count('c')
    a_percent = format((a_picked / len(choices)) * 100, '.4f' )
    b_percent = format((b_picked / len(choices)) * 100, '.4f' )
    c_percent = format((c_picked / len(choices)) * 100, '.4f' )
    a_won = wins.count('a')
    b_won = wins.count('b')
    c_won = wins.count('c')
    a_win_percent = format((a_won / len(wins)) * 100, '.4f' )
    b_win_percent = format((b_won / len(wins)) * 100, '.4f' )
    c_win_percent = format((c_won / len(wins)) * 100, '.4f' )
    win_avg = format((len(wins) / len(choices)) * 100, '.4f')
    # displays results
    if type > 1:
        print("\nResults from picking two doors:\n")
    else:
        print("\nResults from picking one door:\n")
    print("Total wins / percent: " + str(len(wins)) + ' / ' + str(win_avg))
    print("chosen / won: " + "a: " + str(a_percent) + '/' +
          str(a_win_percent) + "  b: " + str(b_percent) + '/' +
          str(b_win_percent) + "  c: " + str(c_percent) + '/' +
          str(c_win_percent))


def main():
    ## simple greeting
    print("Welcome to the Monty Hall Problem!".center(80, '/'))
    # begins timer
    start = time.time()
    w, c = pick_one_door(10)
    do_maths(w, c, 1)
    w, c = pick_two_doors(10)
    do_maths(w, c, 2)
    end = time.time()-start
    print('\nran for:  ' + end + ' seconds\n' + '...fin')

if __name__ == '__main__':
    main()
