# Voglio mostrarvi il concetto di "funzione"
# Una funzione è un blocco di codice
# che può essere chiamato (o richiamato) da
# qualsiasi punto del programma
#
# Quando si chiama una funzione l'esecuzione salta
# alla funzione e la esegue, quando la funzione termina
# l'esecuzione riprende nel punto da dove era partita la chiamata.

def Cavolo():
    print('CAVOLO')

def Salutami():
    print('ciao caro')
    Cavolo()

def Somma(x,y):
    s=x+y
    return s


print(' adesso chiamo la funzione Salutami')
Salutami()
print('la funzione ha finito ed è tornata qua')
som = Somma(3,4.5)
print('La funzione Somma ha ritornato',som)
