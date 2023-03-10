# https://stackoverflow.com/questions/1325581/how-do-i-check-if-im-running-on-windows-in-python

import os
import random
import sys


def intInput(message, validate=None, min_amount=None):
    try:
        v = input(message)
        if v == ':q':
            exit()

        if validate is not None and v not in validate:
            print("Pilihan harus", ", ".join(validate))
            return intInput(message, validate)

        v = int(v)
        if min_amount is not None and v < min_amount:
            print("Input harus lebih dari atau sama dengan",
                  priceFormat(min_amount))
            return intInput(message, validate)

        return v
    # except Exception as e:
    except Exception:
        # raise e
        print("Input harus berupa angka!")
        return intInput(message)


def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def snakeToTitle(string):
    return string.replace('_', ' ').title()


def priceFormat(price):
    price = int(price)
    return (f'IDR {price:,}').replace(',', '.')


def yesNoInput(message):
    v = input(f'{message} [Y / n] ')
    if (v.lower() not in ['y', 'n']):
        print("Input hanya dapat berupa Y / n")
        return yesNoInput(message)

    return v.lower()


def generateRandom(length):
    return ''.join((random.choice('1234567890') for i in range(0, length)))


def writeToTxt():
    sys.stdout = open('output.txt', 'wt')


if __name__ == '__main__':
    print(generateRandom(15))
    print(os.name)
    print(snakeToTitle('test_ea_awokoawk'))
    print(priceFormat(102111))
    yesNoInput("Ulangi?")
    intInput("Masukkan angka : ")
