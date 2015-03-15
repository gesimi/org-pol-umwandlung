__author__ = 'michael.hirsch'

class PolDaten:
    """Wandelt Rohdaten in POL-Daten um
       Beispiele:
       "          10  1.617 190  9800    0.000   0.0000 100.0000"
       "          15  1.300 190  9804  131.635 399.9993  99.7073"
       Die Werte sind:  Schluessel, Höhe, Code, PunktNr, Strecke, HZ, VZ
    """

    def zuPolZeile(self):
        polZeile = '"' + self.schluessel.rjust(12) + self.hoehe.rjust(7) + self.code.rjust(4) + self.punktNr.rjust(6)
        polZeile += self.strecke.rjust(9) + self.hz.rjust(9) + self.vz.rjust(9) + '"'
        self.polZeile = polZeile
        return polZeile

    def __init__(self, orgBlock):
        self.orgBlock = orgBlock
        # nimm 'default' werte, werden ggf. überschrieben
        self.strecke = "0.000"
        self.hz = "0.0000"
        self.vz = "100.0000"
        self.zerlegeOrgBlock(orgBlock)

    def zerlegeOrgBlock(self, orgBlock):
        for eintrag in orgBlock:

            labelWert = eintrag.split("=")

            label = labelWert[0]
            wert = labelWert[1]

            if label == "2":
                self.schluessel = "10"
                self.punktNr = wert

            elif label == "62":
                self.schluessel = "15"
                self.punktNr = wert

            elif label == "5":
                self.schluessel = "20"
                self.punktNr = wert

            elif label == "3":
                self.hoehe = wert

            elif label == "4":
                self.code = wert

            elif label == "6":
                self.hoehe = wert

            elif label == "7":
                self.hz = wert

            elif label == "8":
                self.vz = wert

            elif label == "9":
                self.strecke = wert
