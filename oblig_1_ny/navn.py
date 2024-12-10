# Definerer en funksjon som genererer en introduksjonstekst basert på fornavn, etternavn og alder
def introduksjon(fornavn, etternavn, alder):
    """
    Returnerer en streng med en introduksjon basert på fornavn, etternavn og alder.
    """
    return f'Hei, jeg heter {fornavn} {etternavn} og er {alder} år gammel.'

# Funksjon for å hente inn informasjon fra brukeren
def be_om_informasjon():
    """
    Ber brukeren oppgi fornavn, etternavn og alder. 
    Validerer at alderen er et positivt heltall. 
    Returnerer fornavn, etternavn og alder.
    """
    # Ber brukeren om fornavn, fjerner unødvendige mellomrom og sørger for stor forbokstav
    fornavn = input('Hva er fornavnet ditt? ').strip().capitalize()
    # Ber brukeren om etternavn, fjerner unødvendige mellomrom og sørger for stor forbokstav
    etternavn = input('Hva er etternavnet ditt? ').strip().capitalize()

    # Validerer input for alder
    while True:
        try:
            # Konverterer input til et heltall
            alder = int(input('Hva er alderen din? '))
            # Sjekker at alder ikke er negativ
            if alder < 0:
                print('Alder kan ikke være negativ. Prøv igjen.')
                continue  # Fortsetter loopen til brukeren skriver inn et gyldig tall
            break  # Bryter ut av loopen hvis input er gyldig
        except ValueError:
            # Håndterer feil hvis input ikke er et tall
            print('Vennligst oppgi et gyldig tall for alder.')

    # Returnerer alle tre verdiene
    return fornavn, etternavn, alder

# Hovedflyt av programmet
print("Velkommen til introduksjonsprogrammet!")  # Velkomstmelding til brukeren
fornavn, etternavn, alder = be_om_informasjon()  # Kaller funksjonen for å hente informasjon fra brukeren
print(introduksjon(fornavn, etternavn, alder))  # Genererer og skriver ut introduksjonsteksten
