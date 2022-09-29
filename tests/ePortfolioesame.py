class ContoBanca:
    def __init__(self, denaro, codicesegreto):
        self.denaro = denaro
        self.codicesegreto = codicesegreto

    def getDenaro(self):
        return self.denaro
    def getCodice(self):
        return self.codicesegreto
    def transfer(self):
        if int (input("Inserire il PIN a 5 cifre : "))== self.codice:
            s = input(" Quantità di denaro da trasferire?: ")
            if int(s) > self.denaro:
                print("Impossibile trasferire, importo sul conto insufficiente")
            else:
                print("Denaro Trasferito")
                self.denaro= self.denaro - int(s)
                print("Importo restante: $ " + str(self.denaro))
        else:
            print("Pin Errato")



if __name__ == "__main__":
    cliente = Conto(46732, 3240)
    cliente.transfer()



