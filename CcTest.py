from CC import ContoCorrente

conto = ContoCorrente()
while True:
    try:
        scelta = int(input('Cosa vuoi fare sul conto:\n 1)Visualizza Saldo\n 2)Fai un versamento\n 3)Fai un prelievo\n 4)Visualizza gli ultimi 5\n 5)Esci\n'))
        print()

        if scelta == 1:
            print(conto)
        print()

        if scelta == 2:
            try:
                versamento = int(input("Quanto vuoi versare sul conto corrente:\n"))
                print(conto.setVersamento(versamento))
            except ValueError:
                print('Deve essere un int')
            print()

        if scelta == 3:
            try:
                prelievo = int(input("Quanto vuoi prelevare?\n"))
                print(conto.setPrelievo(prelievo))
            except ValueError:
                print('Deve essere un int')
            print()

        if scelta == 4:
            print(conto.getLast5())
            print()
            
        if scelta == 5:
            break

    except ValueError:
        print("Errore: inserisci un numero per selezionare un'opzione.")
        
    
