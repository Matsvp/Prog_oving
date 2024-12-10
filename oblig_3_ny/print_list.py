def print_list():
    """
    Lager en liste over favorittmat og skriver ut hvert element.
    Returnerer listen.
    """
    list = ['burger', 'pizza', 'taco']  # Definerer listen med favorittmat
    for element in list:  # Itererer gjennom listen
        print(element)  # Skriver ut hvert element
    return list  # Returnerer listen

# Kaller funksjonen og lagrer resultatet i en variabel
liste_med_favoritt_mat = print_list()

# Skriver ut listen lagret i variabelen
print(liste_med_favoritt_mat)
