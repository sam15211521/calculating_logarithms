def squareroot(number, guess):
    return (guess + number/guess) /2

number = input("please enter a number")

current_square_root = 0

while True:
    flag = input(
"""
your number is {number}

what do you want to do?

1. calculate a square root

2. exit""")

    if flag == '1':
        first_guess = input(
"""Please enter a guess on the square root
Your number is:

    {number}

""")
        
    elif flag == '0':
        exit()
    
    else:
        print('not a choice')
