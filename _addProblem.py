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

# ispisati postojece formule za zadatke

problem = input('Unesi tekst zadatka. Varijable upisite u viticaste zagrade. ')
unknown = input('Unesi oznaku nepoznanice u zadatku: ')
const = input('Unesi oznake za konstante koje cete koristiti u zadatku, odvojene razmakom. ')
params = input('Unesi parametre (fiksne vrijednosti) u obliku "velicina: vrijednost", odvijeni zarezom: ')
variables = input('Unesi varijable i raspon u obliku "velicina: min,max,zajednicki faktor". Npr {1000,1100,1200...3100} je 10,31,2; {0.003,0.004...0.008} je 3,8,-3. ')
formulae = []
f = 'x'
while f:
  f = input('Unesi formule koje vrijede za ovaj zadatak, jednu po jednu. Ako nema više formula, stisni enter. ')
  if f != '':
    formulae.append(f)
  
print(problem, unknown, const, params, variables, formulae)
# generirati dict iz toga
p = {}
p['question'] = problem
p['unknown'] = unknown
p['constants'] = const
p['params'] = params
p['knowns'] = variables
p['formulae'] = formulae

print(p)
