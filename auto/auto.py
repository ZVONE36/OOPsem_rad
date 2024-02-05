
#izrada klase auto s definiranim argumentima i metodama

class Auto:
    def __init__(self, auto_id = 0):

        #atributi klase i instanca klase self
        #self - svaki auto ima svoje podatke

        self._drzava_proizvodnje = ""
        self._marka = ""
        self._model = ""
        self._paket = ""
        self._motor = ""
        self._mjenjac = ""
        self._pogon = ""
        self._boja = ""
        self.__id = auto_id
        self.__select_auto_sql = '''SELECT * FROM auto;'''

    #koristenje dekoratora @property i @ime_atributa.setter
    #@property sluzi za dobivanje vrijednosti varijable

    @property
    def id(self):
        return self.__id

    #@ime_argumenta.setter sluzi za postavljanje vrijednosti varijable

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def drzava_proizvodnje (self):
        return self._drzava_proizvodnje

    @drzava_proizvodnje.setter
    def drzava_proizvodnje(self, drzava_proizvodnje):
        self._drzava_proizvodnje = drzava_proizvodnje

    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, marka):
        self._marka = marka

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def paket(self):
        return self._paket

    @paket.setter
    def paket(self, paket):
        self._paket = paket

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def mjenjac(self):
        return self._mjenjac

    @mjenjac.setter
    def mjenjac(self, mjenjac):
        self._mjenjac = mjenjac

    @property
    def pogon(self):
        return self._pogon

    @pogon.setter
    def pogon(self, pogon):
        self._pogon = pogon

    @property
    def boja(self):
        return self._boja

    @boja.setter
    def boja(self, boja):
        self._boja = boja

    def dohvatiAuto(self, cur):
        found = True
        tapl = (self.id,)
        res = cur.execute(self.__select_auto_sql, tapl)
        redak = res.fetchnone()
        if redak is None:
            found = False
        else:
            self.drzava_proizvodnje = redak[0]
            self.marka = redak[1]
            self.model = redak[2]
            self.paket = redak[3]
            self.motor = redak[4]
            self.mjenjac = redak[5]
            self.pogon = redak[6]
            self.boja = redak[7]
        return found

    def ispis_auta(self, cur):
        res = cur.execute(self.__select_auto_sql)
        popis = res.fetchall()
        if popis is not None:
            for i, redak in enumerate(popis, start=1):
                print(f'{i}. {redak[2]} {redak[3]} {redak[4]}')
        else:
            print("Ne postoji auto iz te drzave!")

