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
            
    def pridej_noveho(self):
        nove_jmeno = str(input("Zadejte jméno pojištěného: "))
        nove_prijmeni = str(input("Zadejte přijmení pojištěného: "))
        nove_tel_cislo = str(input("Zadejte telefonní číslo pojištěného: "))
        while len(str(nove_tel_cislo)) != 9:  # aby nedošlo k zadání chybného formátu čísla
            print("Špatný formát telefonního čísla.")
            nove_tel_cislo = str(input("Zadejte znovu telefonní číslo: "))
        novy_vek = int(input("Zadejte věk pojištěného: "))
        while 1 > novy_vek > 100:  # aby nedošlo k chybnému zadání věku
            print("Neplatný věk")
            novy_vek = int(input("Zadejte znovu svůj věk: "))
        novy_pojistenec = Pojistenec(nove_jmeno, nove_prijmeni, nove_tel_cislo, novy_vek) 
        pojistenci.append(novy_pojistenec)
        print(novy_pojistenec)   
        
    def vyhledej_pojisteneho(self):
        vyhledani_jmena = str(input("Zadejte jméno pojištěného: "))
        vyhledani_prijmeni = str(input("Zadejte příjmení pojištěného: "))

        for pojisteni in pojistenci:
            if vyhledani_jmena == pojisteni.jmeno and vyhledani_prijmeni == pojisteni.prijmeni:  # porovnání zadaných hodnot s hodnotami v seznamu
                print(pojisteni)
            else:
                print("Hledaná osoba není v databázi")

        

        
        
adam = Pojistenec("Adam", "Kyselka", "788605211", 37)
marie = Pojistenec("Marie", "Stará", "656711500", 40)
dalibor = Pojistenec("Dalibor", "Novosad", "791523888", 24)
frantisek = Pojistenec("František", "Vrána", "543289791", 68)
pojistenci.append(adam)
pojistenci.append(marie)
pojistenci.append(dalibor)
pojistenci.append(frantisek)


