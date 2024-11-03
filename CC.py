class ContoCorrente():
    def __init__(self, saldo=0):
        saldo = self.setSaldo(saldo)
        self.movimenti = []

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def setVersamento(self, versamento):
        self.__saldo += versamento
        self.movimenti.append({'Movimento':'Versamento', 'Importo':versamento})
        return f"Hai versato: {versamento}, ora hai un saldo di {self.__saldo}"
    
    def setPrelievo(self, prelievo):
        if prelievo > self.__saldo:
            print("Saldo insufficente!")
            return f"Il tuo saldo è di {self.__saldo}"
        else:
            self.__saldo -= prelievo
            self.movimenti.append({'Movimento':'Prelievo', 'Importo':prelievo})
        return f"Hai prelevato {prelievo}, ora il tuo nuovo saldo è: {self.__saldo}"

    def getLast5(self):
        return self.movimenti[-5:]
    
    def __str__(self):
        return f"Il tuo saldo è di: {self.__saldo}"
