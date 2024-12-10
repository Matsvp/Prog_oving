#oppgave 5
print('Dette programmet, finner det største tallet')
def finn_maks(a, b):
    if a > b:
        return a
    elif a < b: 
        return b
    else:
        return "tallene er like"

a = int(input('skriv inn det første tallet :)'))
b = int(input('skriv inn det andre tallet :)'))
print(f'Det største tallet er {finn_maks(a,b)}')

finn_maks(a, b)

# oppgave 6
print('Dette programet sjekker hovr mange bokstaver ordet du skriver inn har')
def tekst_lengde(ord):
    antall_bokstaver = len(ord)
    return antall_bokstaver

ord = input('Skriv inn et ord du vil sjekke antall bokstaver')
print(f'ordet{ord} har {tekst_lengde(ord)} bokstaver')

#oppgave 7 
def sjekk_partall(tall):
    if tall % 2 == 0:
        print('Gratulerer du skrev et partall')
    else:
        print('Du fant ett oddetall')

tall = int(input('Skriv inn et heltall'))
sjekk_partall(tall)
