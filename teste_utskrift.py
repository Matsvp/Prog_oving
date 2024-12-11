import json

# Vi starter med en Python-datastruktur (dictionary) som vi vil konvertere til JSON
person = {
    "navn": "Mats",
    "alder": 19,
    "hobbyer": ["fotball", "gaming", "musikk"]
}

# Konvertere Python dictionary til JSON-streng
person_json_str = json.dumps(person)
print("JSON-streng:", person_json_str)
# Utskrift: JSON-streng: {"navn": "Mats", "alder": 19, "hobbyer": ["fotball", "gaming", "musikk"]}

# Legge merke til at dette nå er en streng i JSON-format.  
# Den kan sendes til en web-server, lagres i en fil, osv.

# Konvertere JSON-streng tilbake til en Python-datastruktur
person_dict = json.loads(person_json_str)

# Nå er 'person_dict' en vanlig Python dictionary igjen
print("Tilbake til dictionary:", person_dict)
# Utskrift: Tilbake til dictionary: {'navn': 'Mats', 'alder': 19, 'hobbyer': ['fotball', 'gaming', 'musikk']}

# Hente ut data
print("Navn:", person_dict["navn"])       # Mats
print("Alder:", person_dict["alder"])     # 19
print("Hobby nr 2:", person_dict["hobbyer"][1])  # gaming

# Eksempel på å skrive JSON til en fil
with open("person.json", "w") as fil:
    json.dump(person, fil)  # Skriver person-dict til person.json i JSON-format

# Eksempel på å lese JSON fra fil
with open("person.json", "r") as fil:
    data = json.load(fil)
    print("Data fra fil:", data)
    # Utskrift: Data fra fil: {'navn': 'Mats', 'alder': 19, 'hobbyer': ['fotball', 'gaming', 'musikk']}

# Oppsummering:
# - json.dumps(objekt) konverterer et Python-objekt til en JSON-streng.
# - json.loads(json_streng) konverterer en JSON-streng til et Python-objekt.
# - json.dump(objekt, fil) skriver et Python-objekt til en fil i JSON-format.
# - json.load(fil) leser JSON fra en fil og returnerer et Python-objekt.


