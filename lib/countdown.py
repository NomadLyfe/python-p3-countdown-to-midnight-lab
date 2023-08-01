import time
def countdown(starting_integer):
    i = starting_integer
    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(starting_integer):
    i = starting_integer
    while i > 0:
        print(f'{i} SECOND(S)!')
        time.sleep(1)
        i -= 1
    print('HAPPY NEW YEAR!')
