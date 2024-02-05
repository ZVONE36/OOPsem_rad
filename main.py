import sqlite3
from auto import Auto
from utilities import unos_intervala, spol_unos, dob_unos
from vozac import Vozac

con = sqlite3.connect('utrka.db')
cur = con.cursor()


running = True
while running:
    print('-' * 20)
    print('1. Ispis svih vozaca')
    print('2. Ispis svih auta')
    print('3. Ispis vozacevog auta')
    print('4. Dodaj novog vozaca')
    print('5. Dodaj novi auto postojecem vozacu')
    print('6. Izbrisi vozaca')
    print('7. Zaustavi program')
    print('-' * 20)

    odabir = unos_intervala(1, 7)

    if odabir == 1:
        ispis_vozaca = '''SELECT ime, prezime FROM vozac;'''
        popis = cur.execute(ispis_vozaca).fetchall()
        print(f'\nPopis vozaca: ')
        for i, redak in enumerate(popis, start=1):
            print(f'{i}. {redak[0]} {redak[1]}')

    elif odabir == 2:
        auto = Auto()
        found = auto.ispis_auta(cur)
        con.commit()

    elif odabir == 3:
        vozac = Vozac()
        vozac_ime = input("Unesite ime vozaca: ")
        found = vozac.dohvatiAuto(vozac_ime, cur)
        con.commit()

    elif odabir == 4:
        novi_vozac = Vozac()
        novi_vozac.ime = input("Unesite ime novog vozaca: ")
        novi_vozac.prezime = input("Unesite prezime novog vozaca: ")
        novi_vozac.spol = spol_unos()
        novi_vozac.dob = dob_unos()
        found = novi_vozac.dodajVozaca(cur, novi_vozac.ime, novi_vozac.prezime, novi_vozac.dob, novi_vozac.spol)
        con.commit()

    elif odabir == 5:
        ispis_vozaca = '''SELECT ime, prezime FROM vozac WHERE id_auto IS NULL;'''
        popis = cur.execute(ispis_vozaca).fetchall()
        print(f'\nPopis vozaca koji nemaju aute: ')
        for i, redak in enumerate(popis, start=1):
            print(f'{i}. {redak[0]} {redak[1]}')
        vozac = Vozac()
        vozac_ime = input("Unesite ime vozaca: ")
        found = vozac.dodajAutovozacu(vozac_ime, cur)

    elif odabir == 6:
        print("Kojeg vozaca zelite izbrisati, upisite ime i prezime")
        ispis_vozaca = '''SELECT ime, prezime FROM vozac;'''
        popis = cur.execute(ispis_vozaca).fetchall()
        print(f'\nPopis vozaca koje mozete izbrisati: ')
        for i, redak in enumerate(popis, start=1):
            print(f'{i}. {redak[0]} {redak[1]}')
        ime = input("Unesite ime: ")
        prezime = input("Unesite prezime: ")
        ime_prezime = (ime, prezime)
        upit = '''DELETE FROM vozac WHERE ime = ? AND prezime = ?;'''
        cur.execute(upit, ime_prezime)
        con.commit()

    elif odabir == 7:
        running = False

