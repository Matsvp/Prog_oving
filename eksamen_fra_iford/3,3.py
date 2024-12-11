def meny():
    return{'ribbe' : 145.90,
           'pinnekjøtt' : 155.90,
           'lutefisk' : 135.90,
           'nøttestek' : 135.90,
           'reinsdyrstek' : 155.90
     }

def place_order(ribbe=0, pinne=0, lute=0, nøtt=0, rein=0):
    # Opprett en dictionary for ordren
    order = {
        'ribbe': ribbe,
        'pinnekjøtt': pinne,
        'lutefisk': lute,
        'nøttestek': nøtt,
        'reinsdyrstek': rein
    }

    if rein > 0:
        print('buuhu')

    return order

def calculate_total(menu, order):
    total_price = 0
    for item, quantity in order.items():
        if item in menu:
            total_price += menu[item] * quantity
    return total_price

def display_cost(menu, order):
    for item, quantity in order.items():  # Iterer over hver rett i bestillingen
        if item in menu:  # Sjekk om retten finnes i menyen
            cost = menu[item] * quantity  # Beregn kostnaden for denne retten
            print(f"{item} - ({quantity}) - {cost:.2f} kr")  # Skriv ut rett, antall og pris

order = place_order(ribbe=2, pinne=3, rein=1)
menu = meny()
total = calculate_total(menu, order)
print(f"Total pris: {total:.2f} kr")
display_cost(menu, order)

def confirm_order(total):
    print(f"Total pris: {total:.2f} kr")
    while True:  # Løkke for å håndtere feil inndata
        valg = input("Vil du godkjenne? (yes/no): ").strip().lower()
        if valg == 'yes':
            print("Rudolf er grønn på nesen!")
            return True
        elif valg == 'no':
            print("Rudolf er rød på nesen!")
            return False
        else:
            print("Ugyldig valg. Skriv enten 'yes' eller 'no'.")
    
    
is_confirmed = confirm_order(total)

print(f"Bekreftelse status: {is_confirmed}")
