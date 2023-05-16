import os

m = [
    ['*','*','*'],
    ['*','*','*'],
    ['*','*','*']
    ]

fine = False
player1 = 'X'
player2 = 'O'
player  = player1
mosse_rimaste=9

def StampaGriglia():
    for i in range(3):
        for j in range(3):
            print(m[i][j],end=' ')
        print()   

#ciclo di gioco
while fine==False:
    os.system('cls') # pulisce lo schermo

    #stampa la griglia
    StampaGriglia()
        
    
    #tiro e verifico mossa
    valida = False
    while valida == False:
        print('riga colonna della mossa, muove:',player)
        r= int(input())
        c= int(input())
        if(m[r][c]=='*'):
            valida = True
    
    #faccio mossa
    m[r][c]=player
    mosse_rimaste=mosse_rimaste-1

    #verifica se vincitore o patta
    tris=False
    for i in range(3):
        if(m[i][0]!='*' and m[i][0]==m[i][1] and m[i][0]==m[i][2]):
            tris=True
                
    for i in range(3):
        if(m[0][i]!='*' and m[0][i]==m[1][i] and m[0][i]==m[2][i]):
            tris=True
                
    if(m[0][0]!='*' and m[0][0]==m[1][1] and m[0][0]==m[2][2]):
        tris=True
            
    if(m[0][2]!='*' and m[0][2]==m[1][1] and m[0][2]==m[2][0]):
        tris=True
            
    if(tris==True):
        fine=True
    elif(mosse_rimaste==0):
        fine=True
    else:
        
        #cambio giocatore
        if(player==player1):
            player=player2
        else:
            player=player1

if(tris==True):
    print('ha vinto il giocatore', player)
else:
    print('partita patta')

       
    
