def legg_til(liste):
    """
    Legger til et element i listen.
    """
    ting = input("Hva vil du legge til? ")
    liste.append(ting)  # Legger til elementet i listen
    print(f'"{ting}" er lagt til i listen.')

def fjern_fra_liste(liste):
    """
    Fjerner et element fra listen hvis det finnes.
    """
    ting = input("Hva vil du ta bort fra listen? ")
    if ting in liste:
        liste.remove(ting)  # Fjerner elementet fra listen
        print(f'"{ting}" er fjernet fra listen.')
    else:
        print(f'"{ting}" finnes ikke i listen.')

def vis_liste(liste):
    """
    Viser alle elementene i listen.
    """
    if liste:
        print("Her er listen:")
        for ting in liste:
            print(ting)
    else:
        print("Listen er tom.")

def main():
    """
    Hovedfunksjonen som håndterer brukerens kommandoer.
    """
    liste = []  # Start med en tom liste

    while True:
        # Tar inn kommandoen fra brukeren
        komando = input('Skriv "L" for å legge til ting, "T" for å fjerne ting, "H" for å vise hele listen, og "stopp" for å stoppe programmet.').lower()

        # Håndterer brukerens kommando
        if komando == "l":
            legg_til(liste)  # Kaller funksjonen for å legge til elementer
        elif komando == "t":
            fjern_fra_liste(liste)  # Kaller funksjonen for å fjerne elementer
        elif komando == "h":
            vis_liste(liste)  # Kaller funksjonen for å vise listen
        elif komando == "stopp":
            print("Programmet er ferdig.")
            print(f'Her er listen: {liste} i tilfelle du trenger det senere :)')
            break  # Avslutter løkken
        else:
            print('Ugyldig kommando. Vennligst skriv "L", "T", "H", eller "stopp".')

        print()  # Legger til en tom linje for å gjøre utdataene mer oversiktlige

# Starter programmet
if __name__ == "__main__":
    main()
