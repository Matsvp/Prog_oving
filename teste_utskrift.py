# --------------------------
# Eksempel med funksjoner, lister og dictionaries
# --------------------------

# Vi starter med en liste over studentnavn.
studenter = ["Mats", "Kari", "Ole", "Lisa"]

# Vi har også et dictionary som skal holde karakterer for hvert fag per student.
# Format:
# karakterer = {
#     "StudentNavn": {
#         "Fag1": Karakter,
#         "Fag2": Karakter,
#         ...
#     },
#     ...
# }
karakterer = {
    "Mats": {"Matte": 4, "Engelsk": 5},
    "Kari": {"Matte": 5, "Engelsk": 3},
    "Ole": {"Matte": 2, "Engelsk": 4},
    "Lisa": {"Matte": 5, "Engelsk": 5}
}
# --------------------------
# Funksjoner
# --------------------------

# 1. Funksjon for å legge til en ny student i "studenter"-listen og
#    legge til en oppføring i "karakterer"-dictionary med tomme fag.
def legg_til_student(navn):
    # Sjekk om studenten allerede finnes
    if navn in studenter:
        print(f"{navn} finnes allerede i listen.")
    else:
        # Legg til studenten i listen
        studenter.append(navn)
        # Opprett en tom dictionary for fagene til den nye studenten
        karakterer[navn] = {}
        print(f"{navn} er lagt til i studentlisten.")

# 2. Funksjon for å sette karakter for en student i et gitt fag
def sett_karakter(navn, fag, karakter):
    # Sjekk om studenten finnes
    if navn in studenter:
        karakterer[navn][fag] = karakter
        print(f"Karakter for {navn} i {fag} er satt til {karakter}.")
    else:
        print(f"{navn} finnes ikke i studentlisten. Kan ikke sette karakter.")

# 3. Funksjon for å hente gjennomsnittskarakter for en student
def hent_gjennomsnitt(navn):
    if navn not in studenter:
        print(f"{navn} finnes ikke.")
        return None

    # Hent dictionary med studentens karakterer
    student_karakterer = karakterer.get(navn, {})
    if not student_karakterer:
        # Ingen karakterer registrert
        print(f"Ingen karakterer er registrert for {navn}.")
        return None

    # Regn ut gjennomsnitt
    total = 0
    antall_fag = 0
    for fag, kar in student_karakterer.items():
        total += kar
        antall_fag += 1

    gjennomsnitt = total / antall_fag
    return gjennomsnitt

# 4. Funksjon for å skrive ut alle studenter og deres karakterer
def skriv_ut_oversikt():
    # Gå gjennom listen med studenter
    for s in studenter:
        # Hent karakterene til studenten
        student_karakterer = karakterer.get(s, {})
        # Skriv ut studentnavn
        print(f"Student: {s}")
        # Hvis ingen fag, si at ingen karakterer er registrert
        if not student_karakterer:
            print("  Ingen karakterer registrert.")
        else:
            # Skriv ut hvert fag og karakter
            for fag, kar in student_karakterer.items():
                print(f"  {fag}: {kar}")
        print()  # Tom linje for luft


# --------------------------
# Bruke funksjonene
# --------------------------

print("----- Før endringer -----")
skriv_ut_oversikt()

# Legge til en ny student
legg_til_student("Per")
# Sett karakterer for Per
sett_karakter("Per", "Matte", 3)
sett_karakter("Per", "Engelsk", 4)

print("----- Etter å ha lagt til Per -----")
skriv_ut_oversikt()

# Oppdatere en eksisterende student sin karakter
sett_karakter("Mats", "Matte", 5)

print("----- Etter oppdatering av karakterer -----")
skriv_ut_oversikt()

# Hente gjennomsnittskarakter for en student
gj_snitt = hent_gjennomsnitt("Lisa")
if gj_snitt is not None:
    print(f"Lisas gjennomsnittskarakter: {gj_snitt:.2f}")

# Prøve å sette karakter for en student som ikke finnes
sett_karakter("Ukjent", "Matte", 4)


# --------------------------
# Oppsummering:
# - Vi startet med en liste "studenter" og et dictionary "karakterer" for å lagre data.
# - Vi lagde funksjoner for å manipulere disse datastrukturene:
#    * legg_til_student(navn): Legger til en ny student i listen og dictionary
#    * sett_karakter(navn, fag, karakter): Setter en karakter for gitt student/fag
#    * hent_gjennomsnitt(navn): Regner ut snittkarakter
#    * skriv_ut_oversikt(): Skriver ut alle studenter og deres karakterer
#
# Dette illustrerer hvordan funksjoner kan strukturere koden, 
# mens lister og dictionaries lagrer og gir tilgang til data.









