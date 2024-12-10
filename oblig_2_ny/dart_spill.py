from random import randrange  # Importerer randrange for å generere tilfeldige poengsummer

def dartspill_en_spiller():
    """
    Simulerer et dartspill for én spiller med tre kast.
    Hvert kast gir mellom 0 og 60 poeng.
    Skriver ut poeng for hvert kast og total poengsum.
    """
    total_score = 0  # Initialiserer total score

    # Gjennomfører 3 kast
    for kast in range(3):  # Løkke som kjører 3 ganger (én gang for hvert kast)
        score = randrange(0, 61)  # Genererer tilfeldig score mellom 0 og 60
        print(f'Kast {kast + 1}: {score} poeng')  # Skriver ut poeng for kastet
        total_score += score  # Legger til poeng for kastet til totalen

    # Skriver ut total poengsum
    print(f'Total score: {total_score} poeng')

# Kaller funksjonen for å starte spillet
# dartspill_en_spiller()


def dartspill_flere_spillere():
    """
    Simulerer et dartspill for flere spillere.
    Hver spiller kaster 3 piler, og deres totale poengsum blir beregnet.
    Skriver ut resultatene for alle spillere.
    """
    antall_spillere = int(input("Hvor mange skal spille? "))  # Spør brukeren om antall spillere

    total_scores = []  # Liste for å lagre total score for hver spiller

    # Itererer gjennom hver spiller
    for spiller_nummer in range(1, antall_spillere + 1):
        print(f'\nSpiller {spiller_nummer} sin tur:')  # Indikerer hvilken spiller som spiller nå
        total_score_more = 0  # Initialiserer total score for denne spilleren

        # Hver spiller kaster 3 piler
        for i in range(3):  # Løkke som kjører 3 ganger for hvert kast
            score = randrange(0, 61)  # Genererer en tilfeldig score mellom 0 og 60
            print(f'Kast {i + 1}: {score} poeng')  # Skriver ut poeng for kastet
            total_score_more += score  # Legger til poengsummen til spillerens totale score

        # Legger til spillerens total score i listen
        total_scores.append(total_score_more)
        print(f"Total score for spiller {spiller_nummer}: {total_score_more} poeng")  # Skriver ut totalscoren for spilleren

    # Skriver ut totalscoren for alle spillere etter at alle har spilt
    print("\nTotale scorer for alle spillere:")
    for spiller_nummer in range(1, antall_spillere + 1):
        print(f'Spiller {spiller_nummer}: {total_scores[spiller_nummer - 1]} poeng')

# Kjør funksjonen for flere spillere
dartspill_flere_spillere()