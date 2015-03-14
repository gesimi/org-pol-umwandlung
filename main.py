__author__ = 'michael.hirsch'

# test zur textverarbeitung

datei = open("161014.org")  # open().readlines gibt liste aus/1 Element = 1 Linie

print("Name der Geodimeter-Datei: ", datei.name)


# text = datei.read()
# print (text)


print(datei)  # funzt so nicht ? doch, gibt info! Typzuweisung string zur ver/bearbeitung ?
# print(type(datei))  # io.TextIOWrapper ? i/o = input/output

# zugriff auf eine linie (line) der eingabedatei, test

polRohDaten = []
index = 0

for line in datei: # was genau ist "line",
    if line[0] == "5":
        print("\t", line.rstrip())
    elif line[0] == "2" and line[1] == "=":
        polRohDaten.append([])
        print(polRohDaten[0])
        polRohDaten[index].append(line)
        # print("\t", line.rstrip())
    elif line[0] == "6" and line[1] == "2":
        index += 1
        polRohDaten.append([])
        polRohDaten[index].append(line)
        # print("\t", line.rstrip())
    # else:

        # print(line.rstrip())

print(polRohDaten)

datei.close()


# testfunktion austausch von werten mit eingabe

def wertzuweisung(wert):
    if wert == "2":  # in "" weil eingabe keine zahl, sondern string, zuweisung int(wert) funzt nicht?
        wert = 10
    elif wert == "62":
        wert = 15
    elif wert == "5":
        wert = 20
        print("haha")

    print("\t", wert)  # return wert/spätere ausgabe funzt hier nicht / (wert) not defined


schluessel = input("Wert?")

wertzuweisung(schluessel)
