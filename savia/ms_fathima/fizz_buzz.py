def fizz_buzz(number):
    message = ''

    if number % 3 == 0:
        message += 'Fizz'

    if number % 5 == 0:
        message += 'Buzz'

    return message