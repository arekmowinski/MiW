# zadanie 1
print("Przypisanie do zmiennej")
zmienna = "Lorem ipsum to roboczy tekst używany do celów projektowych, zwykle do prezentacji kroju pisma, kompozycji, układu kolumn, wyglądu składu, typografii itd."

# zadanie 2
imie = "Arkadiusz"
nazwisko = "Mówiński"

litera_1 = imie[2]
litera_2 = nazwisko[3]

liczba_liter_1 = zmienna.count(litera_1)
liczba_liter_2 = zmienna.count(litera_2)

print("W tekście jest {0} liter {1} oraz {2} liter {3}".format(liczba_liter_1, litera_1, liczba_liter_2, litera_2))

# zadanie 4
zmienna_typu_string = "Lorem Ipsum"

print(dir(zmienna_typu_string))

# zadanie 5
print("Extended Slices Arkadiusz Mówiński:")
print(nazwisko[::-1].capitalize(), imie[::-1].capitalize())

# zadanie 6-7
lista1 = []
for x in range(1, 11):
    lista1.append(x)
print("Lista", lista1)

lista2 = []
for x in lista1[5:]:
    lista2.append(x)
    lista1.remove(x)

print("Listy podzielone: ")
print(lista1, lista2)
lista1.extend(lista2)

print("Połączone: ", lista1)
lista1.insert(0, 0)
print("Dodane zero: ", lista1)
lista1.reverse()
print("Odwrócona: ", lista1)

# zadanie 10
listatel = [8, 8, 2, 2, 0, 0, 3, 3, 5, 5, 9, 9, 1]
unikatowe = set(listatel)
print("Lista numerów:", listatel)
print("Lista unikatowa", unikatowe)

# zadanie 11
listx = []
for x in range(1, 11, 1):
    listx.append(x)
print("Lista 1-10", listx)

# zadanie 12
listy = []
for x in range(100, 19, -5):
    listy.append(x)
print("Lista 100-20", listy)
