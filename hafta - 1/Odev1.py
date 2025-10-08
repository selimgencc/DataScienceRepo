class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def araba_bilgileri(self):
        print(f"Marka: {self.marka}, Model: {self.model}")

araba1 = Araba("Mazda", "MX-5")
araba1.araba_bilgileri()

#---------------------------------------------------------------------------

class Dikdortgen:
    def __init__(self, yukseklik, genislik):
        self.yukseklik = yukseklik
        self.genislik = genislik

    def alan_hesap(self):
        return self.yukseklik * self.genislik

dikdortgen = Dikdortgen(150, 300)
print(dikdortgen.alan_hesap())
alan = dikdortgen.alan_hesap()
print(alan)

#---------------------------------------------------------------------------

class Kare:
    def __init__(self, x):
        self.x = x

    def kare_ciz(self):
        for i in range(self.x):
            print("*" * self.x)

kare = Kare(7)
kare.kare_ciz()

#---------------------------------------------------------------------------

class Hesaplama:
    def topla (self, x, y, z = None):
        if z is not None:
            return x + y + z
        else:
            return x + y

hesap = Hesaplama()
sonuc = hesap.topla(3, 12)
print(sonuc)
sonuc2 = hesap.topla(5, 10, 25)
print(sonuc2)

#---------------------------------------------------------------------------

class Merhaba:
    def merhaba_yaz(self):
        print("Merhaba")

merhaba = Merhaba()
merhaba.merhaba_yaz()

#---------------------------------------------------------------------------