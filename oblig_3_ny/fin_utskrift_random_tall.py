import random  # Importerer random-modulen for å generere tilfeldige tall

def generer_tilfeldig_tall():
    """
    Genererer og returnerer et tilfeldig tall mellom 0 og 99.
    """
    return random.randrange(0, 100)  # Genererer et tilfeldig tall fra 0 (inkludert) til 100 (ikke inkludert)

def vis_tall(tall):
    """
    Viser et tall i en ramme av stjerner.
    """
    print("*********")  # Øverste linje av stjerner for rammen
    print(f"***{tall:03}***")  # Viser tallet med 3 sifre, fylt med ledende nuller hvis nødvendig
    print("*********")  # Nederste linje av stjerner for rammen

def main():
    """
    Genererer og viser tre tilfeldige tall.
    """
    for _ in range(3):  # Gjenta tre ganger (vi ignorerer iterasjonsverdien med '_')
        tall = generer_tilfeldig_tall()  # Kaller funksjonen for å generere et tilfeldig tall
        vis_tall(tall)  # Sender tallet til visningsfunksjonen for å vise det i en ramme

if __name__ == "__main__":  # Sjekker om skriptet kjøres direkte
    main()  # Kaller hovedfunksjonen for å starte programmet

