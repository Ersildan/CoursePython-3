def digits(number):
    for digit in str(number):
        yield int(digit)


def cubed(numbers):
    for number in numbers:
        yield number ** 3


def odds(numbers):
    for number in numbers:
        if number % 2:
            yield number


numbers = cubed(odds(digits(1234321)))

print(*numbers)
