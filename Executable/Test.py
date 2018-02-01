class Spieler ():
    coint = 500
    def __init__(self, name):
        self.name = name
        self.coint = 500

    def gibName(self):
        print (self.name)

    def kauf(self):
        self.coint = self.coint -200

sp1 = Spieler ("Ton")


sp1.gibName()
sp1.kauf()
print(sp1.coint)
