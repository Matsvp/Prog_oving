# Funksjon for å opprette en liste med Tolkien sine bøker
def opprett_tolkien_liste():
    """
    Returnerer en liste med Tolkien sine bøker.
    """
    return [
        "The Hobbit",
        "Farmer Giles of Ham",
        "The Fellowship of the Ring",
        "The Two Towers",
        "The Return of the King",
        "The Adventures of Tom Bombadil",
        "Tree and Leaf"
    ]

# Funksjon for å filtrere Lord of the Rings-trilogien
def legg_til_i_lista_hvis_de_er_lord_triologien(boker):
    """
    Går gjennom listen med bøker og legger til Lord of the Rings-trilogien i en ny liste.
    """
    # Liste over Lord of the Rings-trilogien etter at titlene er endret
    lord_trilogi = [
        "Lord of the Rings: The Fellowship of the Ring",
        "Lord of the Rings: The Two Towers",
        "Lord of the Rings: The Return of the King"
    ]
    ny_liste = []  # Tom liste for å lagre bøker fra Lord of the Rings-trilogien

    # Itererer gjennom listen med bøker for å sjekke om de tilhører trilogien
    for bok in boker:
        if bok in lord_trilogi:
            ny_liste.append(bok)  # Legger til boken i den nye listen
    return ny_liste

# Funksjon for å skrive ut en liste med en elementbasert for-løkke
def skriv_ut_liste_elementbasert(boker):
    """
    Skriver ut innholdet i en liste ved hjelp av en elementbasert for-løkke.
    """
    if not boker:  # Sjekker om listen er tom
        print('Listen er tom')
        return
    print('Lord of the Rings-trilogien:')
    for bok in boker:  # Itererer gjennom listen med bøker
        print(f"- {bok}")  # Skriver ut hver bok

# Funksjon for å skrive ut de to første og de to siste bøkene
def skriv_ut_to_forste_og_to_siste(boker):
    """
    Skriver ut de to første og de to siste bøkene i listen.
    """
    print("De to første bøkene:")
    for bok in boker[:2]:  # Itererer over de to første elementene
        print(f"- {bok}")
    print("De to siste bøkene:")
    for bok in boker[-2:]:  # Itererer over de to siste elementene
        print(f"- {bok}")

# Funksjon for å legge til bøker i listen
def legg_til_boker(boker, nye_boker):
    """
    Legger til nye bøker i listen.
    """
    boker.extend(nye_boker)  # Legger til alle bøkene fra listen `nye_boker`

# Funksjon for å endre Lord of the Rings-trilogien
def endre_lotr_titler(boker):
    """
    Endrer titlene på Lord of the Rings-trilogien for å inkludere 'Lord of the Rings:'.
    """
    for i in range(len(boker)):  # Itererer gjennom listen med indekser
        if boker[i] in [
            "The Fellowship of the Ring",
            "The Two Towers",
            "The Return of the King"
        ]:
            # Oppdaterer tittelen for å inkludere 'Lord of the Rings:'
            boker[i] = f"Lord of the Rings: {boker[i]}"
    return boker

# Funksjon for å sortere listen og skrive den ut
def sorter_og_skriv_ut(boker):
    """
    Sorterer og skriver ut listen med bøker.
    """
    boker.sort()  # Sorterer listen alfabetisk
    print("Sortert liste over Tolkien sine bøker:")
    for bok in boker:  # Itererer gjennom listen
        print(f"- {bok}")  # Skriver ut hver bok

# Hovedprogram
if __name__ == "__main__":
    # Opprett listen med bøker
    tolkien_boker = opprett_tolkien_liste()

    # Skriv ut de to første og de to siste bøkene
    skriv_ut_to_forste_og_to_siste(tolkien_boker)

    # Legg til nye bøker
    nye_boker = ["The Silmarillion", "Unfinished Tales"]
    legg_til_boker(tolkien_boker, nye_boker)

    # Endre titlene på Lord of the Rings-trilogien
    tolkien_boker = endre_lotr_titler(tolkien_boker)

    # Sorter listen og skriv den ut
    sorter_og_skriv_ut(tolkien_boker)

    # Filtrer ut Lord of the Rings-trilogien og skriv den ut
    lotr_boker = legg_til_i_lista_hvis_de_er_lord_triologien(tolkien_boker)
    skriv_ut_liste_elementbasert(lotr_boker)
