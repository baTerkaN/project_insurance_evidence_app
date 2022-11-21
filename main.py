from pojistenec import Pojistenec  # import tříd Pojistenec, Hlavicky
from vypis import Hlavicky
hlavicky = Hlavicky()
pokracovat = True

while pokracovat:  # cyklus vypisovaní aplikace
    print(hlavicky.uvodni_hlavicka())
    print(hlavicky.menu())
    volba = int(input("Napište číslo akce: "))

    if volba == 1:  # přidání nového pojištěného
        Pojistenec.pridej_noveho(Pojistenec)
        input("Data byla uložena. Pokračujte libovolnou klávesou...")
        hlavicky.vycisti_obrazovku()  # vyčistíme si obrazovku od nepotřebného textu

    elif volba == 2:  # vypsání všech pojištěných
        Pojistenec.zobraz_databazi(Pojistenec)  # vypsání všech pojištěnců ze seznamu

        input("Pokračujte libovolnou klávesou...")
        hlavicky.vycisti_obrazovku()

    elif volba == 3:  # vyhledání pojištěného
        vyhledani = Pojistenec.vyhledej_pojisteneho(Pojistenec)
        if len(vyhledani) > 0:  # vypsání hledané osoby
            for pojistenec in vyhledani:
                print(pojistenec)
        else:
            print("Osoba nenalezena.")
        input("Pokračujte libovolnou klávesou...")
        hlavicky.vycisti_obrazovku()

    elif volba == 4:  # ukončení aplikace
        print("Děkujeme za použití naší aplikace.")
        pokracovat = False

    else:  # když se zadá neplatná možnost
        print("Neplatná volba, zadejte číslo od 1 do 4.")
        print(hlavicky.uvodni_hlavicka, hlavicky.menu)
        volba = int(input("Napište číslo akce: "))
