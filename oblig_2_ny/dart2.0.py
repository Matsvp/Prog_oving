from random import choice

# Globale konstanter
GYLDIG_POENG = [0] + list(range(1, 21)) + [2 * i for i in range(1, 21)] + [3 * i for i in range(1, 21)] + [25, 50]
GYLDIGE_DOBLER = [2 * i for i in range(1, 21)]

def hent_antall_spillere():
    """
    Ber brukeren om å angi antall spillere og validerer input.
    """
    while True:
        try:
            antall_spillere = int(input("Hvor mange skal spille? "))
            if antall_spillere > 0:
                return antall_spillere
            print("Antall spillere må være minst 1.")
        except ValueError:
            print("Ugyldig input, skriv inn et tall.")

def start_runde(spiller_nummer, remaining_scores, har_startet):
    """
    Håndterer en spillers runde med tre kast.
    """
    print(f'\nSpiller {spiller_nummer + 1} sin tur:')
    print(f"Spiller {spiller_nummer + 1} har {remaining_scores[spiller_nummer]} poeng igjen.")

    for kast_nummer in range(3):  # Tre kast per runde
        score = choice(GYLDIG_POENG)

        if not har_startet[spiller_nummer]:
            if score in GYLDIGE_DOBLER:  # Spilleren må starte med en dobbel
                har_startet[spiller_nummer] = True
                print(f'Kast {kast_nummer + 1}: {score} poeng - Startet med dobbel!')
            else:
                print(f'Kast {kast_nummer + 1}: {score} poeng - Må treffe dobbel for å starte.')
        else:
            if remaining_scores[spiller_nummer] - score < 0:  # Sjekker om poeng går under 0
                print(f'Kast {kast_nummer + 1}: {score} poeng - Overstiger 0, kast ugyldig.')
            else:
                remaining_scores[spiller_nummer] -= score
                print(f'Kast {kast_nummer + 1}: {score} poeng, gjenstående: {remaining_scores[spiller_nummer]}')
            
            if remaining_scores[spiller_nummer] == 0:  # Spilleren har vunnet
                print(f'\nSpiller {spiller_nummer + 1} vinner!')
                return True  # Returnerer True for å indikere at spillet er over
    return False  # Spilleren har ikke vunnet

def dartspill_flere_spillere():
    """
    Simulerer dartspill for flere spillere.
    """
    antall_spillere = hent_antall_spillere()
    remaining_scores = [301 for _ in range(antall_spillere)]
    har_startet = [False for _ in range(antall_spillere)]

    while True:
        for spiller_nummer in range(antall_spillere):
            if start_runde(spiller_nummer, remaining_scores, har_startet):  # Sjekker om en spiller har vunnet
                return  # Avslutter spillet når noen vinner

def main():
    """
    Hovedprogrammet som starter dartspillet.
    """
    print("Velkommen til dartspillet!")
    dartspill_flere_spillere()

# Starter programmet når skriptet kjøres
if __name__ == "__main__":
    main()