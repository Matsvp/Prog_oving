def hent_positvit_tall(tall):
    while True:
        try:
            verdi = float(input(tall))
            if verdi < 0:
                print('Må vere et positivt tall')
                continue
            return verdi
        except ValueError:
            print("Vennligst skriv inn et gyldig tall.")

def input_variabler():
        H = hent_positvit_tall('Skriv in høyden :)')
        L = hent_positvit_tall('Skriv in lengden :)')
        B = hent_positvit_tall('Skriv in bredden :)')
        return H, L, B
        
    
def regn_ut_volumet(H, L, B):
    return H * L * B

def main():

    høyde, lengde, bredde = input_variabler()
    
    # Beregn volumet
    volum = regn_ut_volumet(høyde, lengde, bredde)
    
    print(f"Volumet av gjenstanden er: {volum:.2f}")

if __name__ == "__main__":
    main()