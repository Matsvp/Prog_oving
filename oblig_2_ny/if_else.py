def sjekk_tall(tall):
    """
    Sjekker om tallet oppfyller spesifikke betingelser og returnerer en melding.
    """
    if tall == 42:
        return "Det stemmer, meningen med livet er 42!"
    elif 30 < tall < 50:
        return "Nærme, men feil."
    elif tall < 0:
        return "Negativt tall! Det kan ikke være riktig."
    elif 10 <= tall <= 20:
        return "Du er på feil spor, men i nærheten av noe interessant!"
    elif tall % 2 == 0:
        return "Det er et partall, men ikke riktig svar."
    else:
        return "FEIL!"

def be_om_tall():
    """
    Ber brukeren om å oppgi et heltall, håndterer ugyldig input, og lar brukeren avslutte.
    """
    while True:
        brukerinndata = input('Skriv inn et heltall (eller skriv "exit" for å avslutte): ')
        if brukerinndata.lower() == "exit":
            print("Avslutter programmet. Ha det bra!")
            exit()  # Stopper programmet
        try:
            tall = int(brukerinndata)
            return tall
        except ValueError:
            print('Vennligst oppgi et gyldig tall.')

# Hovedflyt av programmet
while True:
    tall = be_om_tall()  # Henter tall fra brukeren
    resultat = sjekk_tall(tall)  # Sjekker tallet og lagrer resultatet
    print(f"Du skrev inn: {tall}")
    print(resultat)
