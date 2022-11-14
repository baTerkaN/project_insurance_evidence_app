pojistenci = []


class Pojistenec:
    def __init__(self, jmeno, prijmeni, tel_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel_cislo = tel_cislo
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni}, {self.tel_cislo}, {self.vek}"

    def zobraz_databazi(self):
        for pojistenec in pojistenci:
            print(pojistenec)
            
class NovyPojistenec(Pojistenec):
    def __init__(self, jmeno, prijmeni, tel_cislo, vek):
        super().__init__(jmeno, prijmeni, tel_cislo, vek)

    def pridej_jmeno(self):
        self.jmeno = str(input("Zadejte jméno pojištěného: "))
        pojistenci.append(self.jmeno)
        
    def pridej_prijmeni(self):
        self.prijmeni = str(input("Zadejte přijmení pojištěného: "))
        pojistenci.append(self.prijmeni)
    
    def pridej_tel_cislo(self):
        self.tel_cislo = str(input("Zadejte telefonní číslo pojištěného: "))
        while len(str(self.tel_cislo)) != 9:  # aby nedošlo k zadání chybného formátu čísla
            print("Špatný formát telefonního čísla.")
            self.tel_cislo = str(input("Zadejte znovu telefonní číslo: "))
        pojistenci.append(self.tel_cislo)
            
    def pridej_vek(self):
        self.vek = int(input("Zadejte věk pojištěného: "))
        while 1 > self.vek > 100:  # aby nedošlo k chybnému zadání věku
            print("Neplatný věk")
            self.vek = int(input("Zadejte znovu svůj věk: "))
        pojistenci.append(self.vek)
            
    
        



adam = Pojistenec("Adam", "Kyselka", "788605211", 37)
marie = Pojistenec("Marie", "Stará", "656711500", 40)
dalibor = Pojistenec("Dalibor", "Novosad", "791523888", 24)
frantisek = Pojistenec("František", "Vrána", "543289791", 68)
pojistenci.append(adam)
pojistenci.append(marie)
pojistenci.append(dalibor)
pojistenci.append(frantisek)

