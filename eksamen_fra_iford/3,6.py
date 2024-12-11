import json  # Importer biblioteket for å håndtere JSON-filer

def save_order_to_file(file_name, order):
    with open(file_name, 'w') as file:  # Åpne filen i skrivemodus
        json.dump(order, file)  # Skriv bestillingen til filen i JSON-format
    print(f"Bestillingen er lagret til {file_name}")

def load_order_from_file(file_name):
    try:
        with open(file_name, 'r') as file:  # Åpne filen i lesemodus
            order = json.load(file)  # Last inn JSON-data fra filen
        return order
    except FileNotFoundError:
        print("Fant ikke filen.")
        return None  # Returner `None` hvis filen ikke finnes

# Eksempelbestilling
order = {
    'ribbe': 2,
    'pinnekjøtt': 3,
    'lutefisk': 1,
    'nøttestek': 0,
    'reinsdyrstek': 1
}

# Filnavn
file_name = 'order.json'

# Lagre bestillingen til fil
save_order_to_file(file_name, order)

# Laste inn bestillingen fra fil
loaded_order = load_order_from_file(file_name)
if loaded_order:
    print("Bestillingen som ble lastet inn:", loaded_order)
