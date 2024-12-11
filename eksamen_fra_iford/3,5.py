history_list = []  # Dette er listen der bestillingene skal lagres

def record_order(history_list, order):
    history_list.append(order)  # Legg til bestillingen i historikklisten


# En eksempelbestilling
order1 = {
    'ribbe': 2,
    'pinnekjøtt': 3,
    'lutefisk': 1,
    'nøttestek': 0,
    'reinsdyrstek': 1
}

# Kall funksjonen for å lagre bestillingen
record_order(history_list, order1)

# En ny bestilling
order2 = {
    'ribbe': 1,
    'pinnekjøtt': 0,
    'lutefisk': 2,
    'nøttestek': 1,
    'reinsdyrstek': 0
}

# Lagre den andre bestillingen
record_order(history_list, order2)

# Skriv ut historikklisten
print(history_list)


