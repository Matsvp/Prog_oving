def student_informasjon():
    """
    Returnerer en ordbok med grunnleggende informasjon om en student.
    """
    return {
        "firstname": "ola",  # Studentens fornavn
        "last name": "Nordmann",  # Studentens etternavn
        "favourite course": "Programmering 1"  # Studentens favorittfag
    }

def endre_favoritt_fag(student):
    """
    Lar brukeren oppdatere studentens favorittfag.
    """
    nytt_fag = input("Hva er det nye favorittfaget? ")  # Spør brukeren om nytt favorittfag
    student["favourite course"] = nytt_fag  # Oppdaterer nøkkelen 'favourite course' i student-ordboken
    print(f"Favorittfaget er oppdatert til: {nytt_fag}")  # Bekreftelse på oppdateringen

def gi_studenten_alder(student):
    """
    Lar brukeren legge til studentens alder, og sikrer at alder er gyldig.
    """
    while True:  # Start en løkke for å validere input
        try:
            alder = int(input('Hvor gammel er studenten? '))  # Spør brukeren om alder
            if alder < 0:  # Sjekker om alder er negativ
                print("Alder kan ikke være negativ. Prøv igjen.")
                continue  # Går tilbake til starten av løkken
            student["age"] = alder  # Legger til eller oppdaterer alder i student-ordboken
            print(f'Alder lagt til: {alder}')  # Bekreftelse på oppdateringen
            break  # Bryter ut av løkken hvis input er gyldig
        except ValueError:  # Hvis input ikke er et tall
            print("Vennligst oppgi et gyldig tall for alder.")  # Feilmelding

def vis_student_informasjon(student):
    """
    Skriver ut studentens informasjon på en oversiktlig måte.
    """
    print("\nStudentinformasjon:")  # Skriver ut en overskrift for informasjonen
    for key, value in student.items():  # Itererer over nøkkel-verdi-par i ordboken
        print(f"{key.capitalize()}: {value}")  # Skriver ut hver nøkkel og verdi i et formatert oppsett

# Hovedprogram
def main():
    """
    Håndterer programflyten for å vise, oppdatere og legge til studentinformasjon.
    """
    student = student_informasjon()  # Henter studentens grunnleggende informasjon
    vis_student_informasjon(student)  # Viser informasjon

    endre_favoritt_fag(student)  # Lar brukeren endre favorittfaget
    vis_student_informasjon(student)  # Viser oppdatert informasjon

    gi_studenten_alder(student)  # Lar brukeren legge til alder
    vis_student_informasjon(student)  # Viser oppdatert informasjon

# Starter programmet
if __name__ == "__main__":  # Sikrer at koden under kun kjører når filen kjøres direkte
    main()  # Kaller hovedfunksjonen for å starte programmet
