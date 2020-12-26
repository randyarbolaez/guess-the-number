from random import randint

number_to_guess = randint(0,50)

def sorting_numbers_guessed(data):
    for i in range(1,len(data)):

        key = data[i]
        j = i - 1

        while(j >=0 and data[j] > key):
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

    return data


def error_handling(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print('That\'s not a number!')

def guess_number():
    numbers_guessed = []
    guesses = 0
    while True:
        num = error_handling('What number do you think it is?(0-50) ')
        guesses += 1

        if num in numbers_guessed:
            print('Already guessed that')
            continue
        else:
            numbers_guessed.append(num)
            sorted_numbers_guessed = sorting_numbers_guessed(numbers_guessed)
            numbers_guessed = sorted_numbers_guessed
        if num == number_to_guess:
            print('Correct!!!!!!! :)', ' It took you', guesses, 'guesses')
            return
        if num > number_to_guess:
            print('Too big of a number.')
        else:
            print('That\'s too small')

def main():
    guess_number()


main()
