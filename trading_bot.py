
tom_liste = []



while True:
    try:
        tall = int(input("Skriv inn et tall (eller skriv 'ferdig' for å avslutte): "))
        tom_liste.append(tall)
    except ValueError:
        ferdig = input("Vil du avslutte? (ja/nei): ")
        if ferdig.lower() == 'ja':
            break

største_tall = max(tom_liste)
summen = sum(tom_liste)
print(f'her er listen: {tom_liste}')
print(f'største tallet er: {største_tall}')
print(f'summen av tallene er: {summen}')