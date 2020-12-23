from random import randint

number_to_guess = randint(0,50)

def error_handling(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print('That\'s not a number!')

def guess_number():
    while True:
        num = error_handling('What number do you think it is? ')
        if num == number_to_guess:
            print('Correct!!!!!!! :)' )
            return
        if num > number_to_guess:
            print('Too big of a number.')
        else:
            print('That\'s too small')


def main():
    guess_number()


main()
