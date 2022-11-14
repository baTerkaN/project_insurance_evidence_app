class Hlavicky:
    def uvodni_hlavicka(self):
        return f"--------------------\nEvidence pojištěných\n--------------------\n"

    def menu(self):
        return f"Vyberte si akci:\n1 - Přidat nového pojištěného\n2 - Vypsat všechny pojištěné\n3 - Vyhledat " \
               f"pojištěného\n4 - Konec"

    def vycisti_obrazovku(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])
