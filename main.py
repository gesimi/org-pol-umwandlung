__author__ = 'michael.hirsch'
import pol_daten

datei = open("161014.org")  # open().readlines gibt liste aus/1 Element = 1 Linie
print("Name der Geodimeter-Datei: ", datei.name)

rohDaten = []
index = -1
# index = 0 falls nicht "pass" bei label 50

for zeile in datei:  # was genau ist "line"? ein string!

    zeile = zeile.rstrip("\n")

    if zeile.startswith("50"):
        pass
        # polRohDaten.append([])
        # polRohDaten[index].append(zeile)
    elif zeile.startswith("2="):
        index += 1
        rohDaten.append([])
        rohDaten[index].append(zeile)
    elif zeile.startswith("62") or zeile.startswith("5="):
        # starte neuen block
        index += 1
        rohDaten.append([])
        rohDaten[index].append(zeile)
    elif zeile.startswith("21"):
        pass
    else:
        rohDaten[index].append(zeile)

datei.close()

for block in rohDaten:
    polDaten = pol_daten.PolDaten(block)

    # gui mach was mit polDaten

    print(polDaten.zuPolZeile())



