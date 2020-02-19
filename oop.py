import random
class Mage:
    Nama = "Magi The Clown"
    power = random.randint(0,1001)

    def getName(self):
        return Nama

    def getpower(self):
        return power

class pemain(Mage):
    def debuf(self):
        self.elemen = random.choice(['Light','Dark','Fire','Water','Earth','Wind','Thunder'])
        return self.elemen


mage1 = pemain()
print("namanya adalah " + mage1.Nama + " dia memiliki power " + str(mage1.power) + " Dia memiliki elemen " + mage1.debuf())
