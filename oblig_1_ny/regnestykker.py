# Definerer funksjonen som utfører regnestykker
def regnestykker(a, b, c):
    """
    Utfører en rekke regnestykker med tallene a, b og c, og returnerer resultatene som en dictionary.
    """
    return {
        'stykke_1': a + b * c,                        # Utfører a + (b * c)
        'stykke_2': (a + b) * c,                     # Utfører (a + b) * c
        'stykke_3': a / b / c if b != 0 and c != 0 else "Udefinert (deling på null)",  # (a / b) / c
        'stykke_4': a / (b / c) if b != 0 and c != 0 else "Udefinert (deling på null)" # a / (b / c)
    }

# Funksjon for å skrive ut resultatene
def utregning(resultater):
    """
    Skriver ut alle regnestykkene med deres resultater.
    """
    print("\nResultater av regnestykkene:")
    for operasjon, resultat in resultater.items():
        print(f'{operasjon}: {resultat}')

# Inputverdier
a = 6
b = 3
c = 2

# Utfører beregningene og lagrer resultatene
resultater = regnestykker(a, b, c)

# Skriver ut resultatene
utregning(resultater)