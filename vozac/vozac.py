class Vozac:
    def __init__(self, auto=None):
        self.__id = 0
        self.__ime = ""
        self.__prezime = ""
        self.__spol = ""
        self.__dob = 0
        self.__auto = auto
        self.__select_vozac_sql = '''SELECT id, prezime from vozac WHERE ime = ?;'''
        self.__select_auto_sql = '''SELECT drzava_proizvodnje, marka, model, paket FROM auto INNER JOIN vozac ON vozac.id_auto = auto.id WHERE ime = ?;'''
        self.__insert_vozac_sql = '''INSERT INTO vozac (ime, prezime, spol, dob) VALUES (?,?,?,?);'''

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def spol(self):
        return self.__spol

    @spol.setter
    def spol(self, spol):
        self.__spol = spol

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    @property
    def auto(self):
        return self.__auto

    @auto.setter
    def auto(self, auto):
        self.__auto = auto

    def ispis(self):
        print(f'{self.__ime}, {self.__prezime}')

    def dodajVozaca(self, cur, ime, prezime, dob, spol):

        novi_vozac = (self.ime, self.prezime, self.spol, self.dob)
        imena_iz_baze = '''SELECT ime, prezime from vozac WHERE ime = ? AND prezime = ? AND dob = ?;'''
        cur.execute(imena_iz_baze, (self.ime, self.prezime, self.dob))
        redak = cur.fetchone()
        if redak:
            raise Exception("Ime vec postoji!")
        else:
            cur.execute(self.__insert_vozac_sql, novi_vozac)
            return

    def dohvatiAuto(self, vozac_ime, cur):
        res = cur.execute(self.__select_auto_sql, (vozac_ime, ))
        redak = res.fetchone()
        if redak is not None:
            return print(f'Drzava proizvodnje: {redak[0]}\nMarka: {redak[1]}\nModel: {redak[2]}\nPaket: {redak[3]}')
        else:
            print("Vozac ne posjeduje auto")
            exit(1)

    def dodajAutovozacu(self, ime, cur):
        found = True
        vozac_ime = (ime,)
        res = cur.execute(self.__select_vozac_sql, vozac_ime)
        redak = res.fetchone()

        if redak is None:
            found = None
        else:
            vozac_id = redak[0]
            upit = '''SELECT * FROM auto;'''
            res = cur.execute(upit)
            popis = res.fetchall()
            print("Popis automobila:")
            for i, redak in enumerate(popis, start=1):
                print(f'{i}. {redak[2]} {redak[3]} {redak[4]}')
            auto = int(input("Odaberite redni broj automobila: "))


            unos = f'''UPDATE vozac SET id_auto = {auto} WHERE id = {vozac_id};'''

            res = cur.execute(unos)

            return found
