# Oppgave 1
def skriv_hilsen():
    print('Velkommen til Python-programmering!')

skriv_hilsen()

# Oppgave 2
def skriv_navnet(navn):
    if not navn.isalpha():  # Sjekker om navnet kun inneholder bokstaver
        print('Navn kan kun inneholde bokstaver.')
    else:
        print(f'Hei {navn}!')

navn = input('Hva heter du? ')
skriv_navnet(navn)

# Oppgave 3
def dobbel_tall(x):
    return x * 2  # Returnerer resultatet i stedet for å skrive det ut

try:
    x = float(input('Skriv inn et tall som du vil doble: '))
    print(f'Doblet tall: {dobbel_tall(x)}')
except ValueError:
    print('Vennligst skriv inn et gyldig tall.')

# Oppgave 4
def summer_tall(tall_1, tall_2):
    return tall_1 + tall_2  # Returnerer summen

try:
    tall_1 = float(input('Skriv inn det første tallet: '))
    tall_2 = float(input('Skriv inn det andre tallet: '))
    print(f'Summen av tallene er {summer_tall(tall_1, tall_2)}')
except ValueError:
    print('Vennligst skriv inn gyldige tall.')
