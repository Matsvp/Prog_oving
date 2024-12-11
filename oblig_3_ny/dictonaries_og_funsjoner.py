def filmer():
    """
    Returnerer en liste over filmer med tittel, årstall og rating.
    """
    return [
        {"tittel": "Inception", "aar": 2010, "rating": 8.7}, 
        {"tittel": "Inside Out", "aar": 2015, "rating": 8.1},
        {"tittel": "Con Air", "aar": 1997},  # Ingen rating definert
    ]

def legg_til_filmer(filmliste, standard_rating=5.0):
    """
    Lar brukeren legge til en ny film i listen.
    Tildeler standardrating hvis brukeren ikke spesifiserer en rating.
    """
    tittel = input("Hva er tittelen på filmen? ")  # Ber om filmtittel
    while True:
        try:
            aar = int(input("Hvilket år ble filmen utgitt? "))  # Ber om årstall
            break
        except ValueError:
            print("Vennligst skriv inn et gyldig år.")
    
    while True:
        try:
            rating = input("Hva er filmens rating? (1.0 - 10.0 eller la være tomt for standardrating) ")
            if not rating:  # Hvis ratingen er tom
                rating = standard_rating  # Setter standardrating
                break
            rating = float(rating)  # Konverterer til desimaltall
            if 1.0 <= rating <= 10.0:  # Sjekker at ratingen er gyldig
                break
            print("Rating må være mellom 1.0 og 10.0.")
        except ValueError:
            print("Vennligst skriv inn en gyldig rating.")
    
    ny_film = {"tittel": tittel, "aar": aar, "rating": rating}  # Oppretter en ny film som ordbok
    filmliste.append(ny_film)  # Legger til filmen i listen
    print(f"Filmen '{tittel}' er lagt til med rating {rating}.")

def default_ratingen(filmliste, standard_rating=5.0):
    """
    Oppdaterer filmer uten rating med en standardrating.
    """
    for film in filmliste:
        if "rating" not in film:  # Sjekker om filmen mangler rating
            film["rating"] = standard_rating  # Setter standardrating
    print(f"Alle filmer uten rating har fått standardrating {standard_rating}.")

def vis_filmer(filmliste):
    """
    Skriver ut alle filmer i en oversiktlig liste.
    """
    print("\nFilmer:")
    for film in filmliste:
        rating = film.get("rating", "Ikke definert")  # Henter rating, eller viser "Ikke definert" hvis den mangler
        print(f"{film['tittel']} ({film['aar']}) - Rating: {rating}")

def gjennomsitsrating(filmliste):
    total_rating = 0
    antall_filmer = len(filmliste)
    if antall_filmer == 0:
        return 0
    
    for film in filmliste: 
        total_rating += film['rating']
    
    return total_rating / antall_filmer


def filmer_fra_og_med_aar(filmliste, aarstall):
    return[film for film in filmliste if film['aar'] >= aarstall]

# Hovedprogram
def main():
    filmliste = filmer()  # Henter listen over filmer
    vis_filmer(filmliste)  # Viser de eksisterende filmene

    # Gi standardrating til filmer uten rating
    default_ratingen(filmliste)
    vis_filmer(filmliste)  # Viser listen med oppdaterte ratinger

    while True:
        print("\nHva vil du gjøre?")
        print("1. Legge til en film")
        print("2. Se alle filmer")
        print("3. Beregn gjennomsnittlig rating")
        print("4  Liste med filmer etter 2010")
        print("5. Avslutt")
    
        valg = input("Velg et alternativ (1-5): ")
        
        if valg == "1":
            legg_til_filmer(filmliste)  # Legger til film og gir standardrating om nødvendig
        elif valg == "2":
            vis_filmer(filmliste)
        elif valg == "3":
            gjennomsnitt = gjennomsitsrating(filmliste)  # Beregner gjennomsnitt
            print(f"Gjennomsnittlig rating for filmer: {gjennomsnitt:.2f}")
        elif valg == "4":
            filmer_2010_og_senere = filmer_fra_og_med_aar(filmliste, 2010)
            print("\nFilmer fra og med 2010:")
            for film in filmer_2010_og_senere:
                print(f"Tittel: {film['tittel']}, År: {film['aar']}, Rating: {film['rating']}")
        elif valg == "5":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    main()
