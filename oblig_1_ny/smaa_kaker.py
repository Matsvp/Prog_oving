def antall_smaa_kaker():
    """
    Returnerer en ordbok med antall småkaker spist av hver person.
    """
    return {
        'person_1': 5,      # Person 1 har spist 5 småkaker
        'person_2': 9,      # Person 2 har spist 9 småkaker
        'person_3': 2.5,    # Person 3 har spist 2.5 småkaker
        'person_4': 21,     # Person 4 har spist 21 småkaker
        'person_5': 0       # Person 5 har spist 0 småkaker
    }

def regn_ut_gjennomsnitt():
    """
    Beregner gjennomsnittlig antall småkaker spist per person.
    """
    personer = antall_smaa_kaker()  # Henter ordboken som inneholder småkaker per person
    totale_kaker = sum(personer.values())  # Summerer antall småkaker spist av alle personer
    antall_personer = len(personer)  # Teller antall personer i ordboken
    gjennomsnitt = totale_kaker / antall_personer  # Beregner gjennomsnittet
    return gjennomsnitt  # Returnerer gjennomsnittet

# Kaller funksjonen for å beregne gjennomsnittet og konverterer til heltall
gjennomsnitt = int(regn_ut_gjennomsnitt())

# Skriver ut resultatet som et heltall
print(f"Gjennomsnittlig antall småkaker per person er: {gjennomsnitt}")
