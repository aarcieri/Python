import os

m = [
    ['*','*','*'],
    ['*','*','*'],
    ['*','*','*']
    ]

player1 = 'X'
player2 = 'O'

def StampaGriglia(m):
    for i in range(3):
        for j in range(3):
            print(m[i][j],end=' ')
        print()   

def Tira(player):
    valida = False
    while valida == False:
        print('riga colonna della mossa, muove:',player)
        r= int(input())
        c= int(input())
        if(m[r][c]=='*'):
            valida = True
    return r, c

def VerificaVincita(m):
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

    return tris

def CambiaPlayer(player):
    if(player==player1):
        player=player2
    else:
        player=player1
    return player

def Gioco():
    mosse_rimaste = 9    
    player = player1
    fine   = False
    #ciclo di gioco
    while not fine:
        os.system('cls') # pulisce lo schermo

        StampaGriglia(m) #stampa la griglia
        
        r,c = Tira(player) #tiro e verifico mossa
    
        #faccio mossa
        m[r][c]=player
        mosse_rimaste=mosse_rimaste-1

        tris = VerificaVincita(m)#verifica se vincitore o patta
            
        if(tris or mosse_rimaste==0):
            fine=True
        else:
            player=CambiaPlayer(player) #cambio giocatore

    if(tris==True):
        print('ha vinto il giocatore', player)
    else:
        print('partita patta')

Gioco()

       
    
