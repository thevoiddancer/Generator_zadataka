from _folders import *

print("Odaberi razred")
for i, folder in enumerate(getFolders()):
    print(chr(ord('a') + i), folder)
razred = input("Unesi slovo za razred: ")
while len(razred) != 1 or razred not in "abcdef"[:len(getFolders())]:
    razred = input("Krivi unos. Unesi ponovo: ")
path = getFolders()[ord(razred)-ord('a')] + "/"

print("Odaberi cjelinu")
for i, folder in enumerate(getFolders(path)):
    print(chr(ord('a') + i), folder)
cjelina = input("Unesi slovo za cjelinu: ")
while len(cjelina) != 1 or cjelina not in "abcdefghij"[:len(getFolders(path))]:
    cjelina = input("Krivi unos. Unesi ponovo: ")
path += getFolders(path)[ord(cjelina)-ord('a')] + "/"

print("Odaberi tip zadatka")
for i, file in enumerate(os.scandir(path)):
    print(chr(ord('a') + i), file.name)
zadatak = input("Unesi slovo za zadatke: ")
while len(zadatak) != 1 or zadatak not in "abcdefghij"[:len(list(os.scandir(path)))]:
    zadatak = input("Krivi unos. Unesi ponovo: ")
path += list(os.scandir(path))[ord(zadatak)-ord('a')].name

