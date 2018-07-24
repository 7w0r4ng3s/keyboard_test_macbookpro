# to test not functional keys of macbook pro 2016 & 2017 with butterfly keyboard
from termcolor import colored

# the correct number of functional keys
letters_26 = 'qwertyuiopasdfghjklzxcvbnm'
letter_test = input('Type 26 letters:\n')
# the correct number of functional number keys
num_10 = '1234567890'
num_test = input('Type 10 numbers:\n')

# Problem1: Letters or characters do not appear
appear_problem = False
# Problem2: Letters or characters repeat unexpectedly
repeat_problem = True

num_key_problem1 = False
letter_key_problem1 = False
both_problem1 = False


def key_appear_problem():
    global num_key_problem1
    global letter_key_problem1
    global both_problem1
    global appear_problem
    # correct letters & nums length > input length
    # detect the difference
    if num_test == num_10 and letter_test == letters_26:
        print(colored('NO_ERRORS', 'green'))
    elif not num_test == num_10 and letter_test == letters_26:
        print(colored('A number key is not functioning', 'blue'))
        num_key_problem1 = True
    elif num_test == num_10 and not letter_test == letters_26:
        print(colored('A letter key is not functioning', 'red'))
        letter_key_problem1 = True
    else:
        print(colored('Both have keys with problems', 'blue', 'on_red'))
        both_problem1 = True
    appear_problem = True


print()
key_appear_problem()


# detect the damaged key
def diff_num_key():
    tmp = []
    for char in num_10:
        if char not in num_test:
            tmp.append(char)
    print('Damaged number keys:')
    print(*tmp, sep=', ')


def diff_letter_key():
    tmp = []
    for char in letters_26:
        if char not in letter_test:
            tmp.append(char)
    print('Damaged letter keys:')
    print(*tmp, sep=', ')


if num_key_problem1:
    diff_num_key()
elif letter_key_problem1:
    diff_letter_key()
elif both_problem1:
    diff_letter_key()
    diff_num_key()
