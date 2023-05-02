import random

numeri=[-8,0,3,-5,91]  # questa è una lista (in python)
for n in numeri:
    print(i)

for n in numeri:
    print(n)

    
print(numeri[0])
print(numeri[4])
print(n) # visualizza 91

del n # cancella n

numeri.pop(0) # toglie -8
numeri.pop(0) # toglie 0
numeri.pop(0) # toglie 3
numeri.pop(0) #toglie -5
numeri.pop(0) #toglie 91

print(numeri) # visualizza []
print(len(numeri)) # visualizza 0


for i in range(0,5):
    numeri.append(random.randint(0,100))

    
# numeri  è per esmpio [36, 21, 5, 54, 4]
numeri.insert(2,-1)
# numeri è diventato [36, 21, -1, 5, 54, 4]
numeri=[] #svuoto la lista, la ricreiamo

