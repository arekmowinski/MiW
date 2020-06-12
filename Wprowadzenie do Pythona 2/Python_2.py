# Zadanie 1

a_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ab_list = []

def zad1(a_list, b_list):
    ab_list = [i for i, j in enumerate(a_list) if i % 2 == 0]
    ab_list += [i for i, j in enumerate(b_list) if i % 2 == 1]
    return print(ab_list)


zad1(a_list, b_list)


# Zadanie 2

def zad2(data_text):
    length = len(data_text)
    letters = list(data_text)
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    dict = {
        'length': length,
        'letters': letters,
        'big_letters': big_letters,
        'small_letters': small_letters
    }
    return print(dict)


zad2('Moto')


# Zadanie 3

def zad3(text, letter):
    wynik = text.replace(letter, '')
    return print(wynik)


zad3('kajak', 'k')


# Zadanie 4

def zad4(stopnie_celsjusza, temperature_type):
    if temperature_type == 'Fahrenheit':
        wynik = (stopnie_celsjusza * 9 / 5) + 32
        return print(wynik)
    elif temperature_type == 'Rankine':
        wynik = (stopnie_celsjusza * 9 / 5) + 491.67
        return print(wynik)
    elif temperature_type == 'Kelvin':
        wynik = stopnie_celsjusza + 273.15
        return print(wynik)
    else:
        return print('Błąd! Proszę podać prawdiłowy typ temperatury')


zad4(4, 'Fahrenheit')
zad4(4, 'Rankine')
zad4(4, 'Kelvin')
zad4(4, '???')


# Zadanie 5

class Calculator:
    def add(a, b):
        wynik = a + b
        return print(wynik)

    def difference(a, b):
        wynik = a - b
        return print(wynik)

    def multiply(a, b):
        wynik = a * b
        return print(wynik)

    def divide(a, b):
        wynik = a / b
        return print(wynik)


Calculator.add(1, 1)
Calculator.difference(6, 2)
Calculator.multiply(3, 2)
Calculator.divide(16, 2)


# Zadanie 6

class ScienceCalculator(Calculator):
    def exponentiation(a, b):
        wynik = a ** b
        return print(wynik)


ScienceCalculator.exponentiation(2, 4)


# Zadanie 7

def ćw7(tekst):
    tekst_od_tyłu = tekst[::-1]
    return print(tekst_od_tyłu)

ćw7('koteł')



# Zadanie 8-9

from file_manager import FileManager

plik = FileManager("plik.txt")

FileManager.read_file(plik)
FileManager.update_file(plik, " oraz tekst, który został dopisany")
FileManager.read_file(plik)

