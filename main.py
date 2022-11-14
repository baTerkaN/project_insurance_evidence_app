from pojistenec import Pojistenec, NovyPojistenec, pojistenci  # import tříd Pojistenec, Hlavicky a seznam pojistenci
from vypis import Hlavicky
hlavicky=Hlavicky() 
pokracovat = True

while pokracovat:
    print(hlavicky.uvodni_hlavicka())
    print(hlavicky.menu())
    volba = int(input("Napište číslo akce: "))

    if volba == 1:  # přidání nového pojištěného
        NovyPojistenec.pridej_jmeno(NovyPojistenec)
        NovyPojistenec.pridej_prijmeni(NovyPojistenec)
        NovyPojistenec.pridej_tel_cislo(NovyPojistenec)
        NovyPojistenec.pridej_vek(NovyPojistenec)
        input("Data byla uložena. Pokračujte libovolnou klávesou...")
        hlavicky.vycisti_obrazovku()  # vyčistíme si obrazovku od nepotřebného textu
        
        

    elif volba == 2:  # vypsání všech pojištěných
        Pojistenec.zobraz_databazi(Pojistenec)  # vypsání všech pojištěnců ze seznamu

        input("Pokračujte libovolnou klávesou...")
        hlavicky.vycisti_obrazovku()
        

    elif volba == 3:  # vyhledání pojištěného
        vyhledani_jmena = str(input("Zadejte jméno pojištěného: "))
        vyhledani_prijmeni = str(input("Zadejte příjmení pojištěného: "))

        for pojisteni in pojistenci:
            if vyhledani_jmena == pojisteni.jmeno and vyhledani_prijmeni == pojisteni.prijmeni:  # porovnání zadaných hodnot s hodnotami v seznamu
                print(pojisteni)

        input("Pokračujte libovolnou klávesou...")
        hlavicky.vycisti_obrazovku()
        

    elif volba == 4:  # ukončení aplikace
        print("Děkujeme za použití naší aplikace.")
        pokracovat = False

    else:  # když se zadá neplatná možnost
        print("Neplatná volba, zadejte číslo od 1 do 4.")
        print(hlavicky.uvodni_hlavicka, hlavicky.menu)
        volba = int(input("Napište číslo akce: "))
