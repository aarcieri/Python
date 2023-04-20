# dato un numero n
# fa la somma 0+1+2+3+...+n

# esempio: n=4 la somma è
# 0+1+2+3+4=10

somma=0
print('inserisci un numero')
n=input() # ??? input()
          # preleva caratteri
          # non numeri
n=int(n) #cosi n diventa un numero

for i in range(0,n+1):
    if(i%2==0):
        somma = somma + i
        
print(somma)
        

print('la somma è', somma)
