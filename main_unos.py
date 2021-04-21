'''
0. odabir u koji file
1. tekst s poljima
2. velicina koja se trazi
3. poznate velicime
  a) konstante
  b) parametri
  c) random velicine
4. dodatne formule
5. potvrda

'''

# 0. odabir filea
# perurediti za genericko
#for i in range(1, 6):
  #print('z{}.txt'.format(i))
# omoguciti provjeru i potvrdu
#num = int(input('Odaberi zadatak za dodati'))
#with open('z{}.txt'.input(num), 'a') as file:

import re
special = '[CEINOQS](?!_)'

for i in range(1):
    question = input('Unesi pitanje s varijablama unutar vitičastih zagrada. Indeksiraj varijable ako nisu u SI sustavu. ')
    print('Unesi formule specifične za zadatak, jednu po jednu. Kada si gotov, lupi ENTER.')
    formulae = []
    formula = input('formula: ')
    while formula:
        formulae.append(formula)
        formula = input('formula: ')
    unknown = input('Koja veličina se traži? ')
    constants = input('Unesi oznake za univerzalne konstante koje se koriste, odvojene zarezom. Ako ne koristiš konstante, lupi ENTER. ')
    constants = constants if constants else []
    print('Unesi parametre, prvo simbol pa onda vrijednost. Kada si gotov, lupi ENTER.')
    parameters = {}
    symbol = input('Unesi simbol: ')
    while symbol:
        value = float(input('{} = '.format(symbol)))
        value = int(float(value)) if float.is_integer(float(value)) else float(value)
        parameters[symbol] = value
        symbol = input('Unesi simbol: ')
    print('Unesi zadane veličine u formatu "od, do, exp" gdje od i do predstavljaju minimum i maksimum slučajnih brojeva, a exp je zajednički znanstveni eksponent. Npr: stotice između 200 i 700: (2, 7, 2); između 3 i 9 nm: (3, 9, -9); valna duljina svjetlosti u desecima nm: (40, 75, 1-9)...')
    knowns = {}
    symbol = input('Unesi simbol: ')
    while symbol:
        value = input('Unesi opseg vrijednosti za {}: '.format(symbol))
        knowns[symbol] = value
        symbol = input('Unesi simbol: ')
    
    q = {'question': question, 'unknown': unknown, 'constants': constants,
         'parameters': parameters, 'formulae': formulae, 'knowns': knowns}
    match = re.findall(special, str(q))
    print(q)
    if match:
        print("Detektirani su znakovi koji se sukobljuju sa sympyevim internim znakovima. Na postojeće znakove dodaje se indeks 1.")
        for item in match:
            q = eval(re.sub(special, item+"_1", str(q), count=1))
    print(q)
