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

order = place_order(ribbe=2, pinne=3, rein=1)
print(order)

