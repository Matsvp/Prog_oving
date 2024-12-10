def for_løkke_oddetall():
    """
    Genererer en liste med oddetall fra 9 til 100 ved hjelp av en for-løkke.
    """
    oddetall = []  # Initialiserer en tom liste for å lagre oddetall
    for tall in range(9, 101, 2):  # Itererer fra 9 til 100, hopper med 2 for å få bare oddetall
        oddetall.append(tall)  # Legger hvert oddetall til listen
    return oddetall  # Returnerer listen med oddetall

def while_løkke_oddetall():
    """
    Genererer en liste med oddetall fra 9 til 100 ved hjelp av en while-løkke.
    """
    tall = 9  # Starter med første oddetall
    oddetall = []  # Initialiserer en tom liste for å lagre oddetall
    while tall < 101:  # Løkken fortsetter så lenge tall er mindre enn 101
        if tall % 2 != 0:  # Sjekker om tallet er et oddetall
            oddetall.append(tall)  # Legger til oddetall i listen
        tall += 1  # Øker tallet med 1 for å fortsette til neste tall
    return oddetall  # Returnerer listen med oddetall

# Kaller for-løkke-funksjonen og lagrer resultatet i en variabel
for_løkke = for_løkke_oddetall()

# Kaller while-løkke-funksjonen og lagrer resultatet i en variabel
while_løkke = while_løkke_oddetall()

# Skriver ut resultatene fra begge løkkene
print(f'Her er For-Løkka {for_løkke}')  # Skriver ut listen med oddetall fra for-løkka
print(f'Her er While-løkka {while_løkke}')  # Skriver ut listen med oddetall fra while-løkka
