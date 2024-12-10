def hent_tall(tall):
    """
    Ber brukeren oppgi et tall og håndterer ugyldig input.
    """
    while True:
        try:
            return float(input(tall))
        except ValueError:
            print("Vennligst skriv inn et gyldig tall.")

def kalkuler (tall_1, tall_2):
    """
    Utfører ulike matematiske operasjoner på to tall og returnerer resultatene som en dictionary.
    """
    return {
        "pluss": tall_1 + tall_2,
        "minus": tall_1 - tall_2,
        "gange": tall_1 * tall_2,
        "dele": tall_1 / tall_2 if tall_2 != 0 else "Udefinert (kan ikke dele på null)",
        "modulo": tall_1 % tall_2 if tall_2 != 0 else "Udefinert (kan ikke finne resten med null)",
        "opphøying": tall_1 ** tall_2,
        "heltallsdivisjon": tall_1 // tall_2 if tall_2 != 0 else "Udefinert (kan ikke dele heltallsvis med null)"
    }

def skriv_resultater(resultater, tall_1, tall_2):
    """
    Skriver ut resultatene av de ulike operasjonene.
    """
    for opperasjon, resultat in resultater.items():
         print(f'{tall_1} {opperasjon} {tall_2} = {resultat}')


# Henter tall fra brukeren
tall_1 = hent_tall("Skriv inn det første tallet: ")
tall_2 = hent_tall("Skriv inn det andre tallet: ")

# Utfører beregninger
resultater = kalkuler(tall_1, tall_2)

# Skriver ut resultatene
skriv_resultater(resultater, tall_1, tall_2)