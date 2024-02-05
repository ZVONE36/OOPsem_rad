
def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj<min or broj>max:
                raise Exception(f"Unesite broj unutar intervala {min}-{max}.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def dob_unos():
    while True:
        try:
            dob = int(input("Unesite dob vozača: "))
            if dob < 18 or dob > 50:
                raise ValueError("Ne smijete voziti!")
            return dob
        except ValueError as e:
            print(f"Pogreška: {e}. Pokušajte ponovno.")



def spol_unos():
        while True:
            try:
                spol = input("Unesite spol vozača: ")

                # Provjera je li uneseni spol string
                if not isinstance(spol, str):
                    raise ValueError("Spol mora biti string!")

                # Provjera je li uneseni spol prazan string
                if not spol.strip():
                    raise ValueError("Uneseni spol ne može biti prazan string.")

                # Provjera je li uneseni spol integer
                if spol.isdigit():
                    raise ValueError("Spol ne može biti broj!")

                # Ako je sve u redu s unosom, vrati spol i prekini petlju
                return spol
            except ValueError as e:
                print(f"Pogreška: {e}. Pokušajte ponovno.")
