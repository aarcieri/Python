import fitz
import os
from random import randint

SEP    = '#'
OK     = True
ERRATO = False

os.chdir('/home/antonio/Scrivania/Scuola/Scuola_2021-2022/PRESIDI')

def RimuoviNumeroPagina(s, ultimaPagina):
    s=s.strip()
    pagina=True
    end='/'+str(ultimaPagina)
    if(s.count(end)==0): return s.strip()
    slash=s.index(end)
    digit=0
    j=slash-1
    while(j>=0 and ord(s[j])>=48 and ord(s[j])<=57):
       j-=1
       digit+=1

    s=s[:slash-digit]+s[slash+len('/1453'):]
    s=s.replace('  ',' ')

    return s.strip()

def __EstraiFile():
    area = []

    for i in range(1,10):
        #print('create file: ', 'area_'+str(i)+'.csv')
        area.append(open('area_'+str(i)+'.csv', 'w'))

    text=''
    num=0
    testo=''
    risposte=''
    i=0
    with fitz.open("Domande della Prova Preselettiva.pdf") as doc:
        for page in doc:
            text+=page.get_text()
  
    lines=text.splitlines()

    while(i<len(lines)):
        if(lines[i].startswith('DOMANDA ')):
            num = lines[i]
            x = int(float(num.split()[1]))
            testo=''
            risposte=''
            i+=1
            while(lines[i][0]!='['):
                testo+=' ' +lines[i]
                i+=1
            while(not lines[i].startswith('[d]')):
                  risposte+=' ' +lines[i]
                  i+=1
            while(i<len(lines) and not lines[i].startswith('[RIF.')):
                risposte+=' ' +lines[i]
                i+=1
            #if(num=='DOMANDA 7.17'): print('-'+testo+'-')
            risposte=risposte.strip()
            testo=RimuoviNumeroPagina(testo, 1453)
            #if(num=='DOMANDA 7.17'): print('-'+testo+'-')
            a=RimuoviNumeroPagina(risposte[3:risposte.index('[b')], 1453)
            b=RimuoviNumeroPagina(risposte[risposte.index('[b')+3:risposte.index('[c')], 1453)
            c=RimuoviNumeroPagina(risposte[risposte.index('[c')+3:risposte.index('[d')], 1453)
            d=RimuoviNumeroPagina(risposte[risposte.index('[d')+3:], 1453)
            #if(num=='DOMANDA 7.11'): print(testo, a,b,c,d)           
            area[x-1].write(num+SEP+ testo+SEP+a+SEP+b+SEP+c+SEP+d+'\n')
            area[x-1].flush()
        else: i+=1
    print('Fine Caricamento FILE')

def __CaricaArea(area):
    quesiti=[]
    f=open('area_'+str(area)+'.csv', 'r')
    l=f.readline().split(SEP)
    while(l[0]!=''):
        num = l[0].split('.')[1]
        #print(num)
        l[0]=int(num)
        quesiti.append(l)
        l=f.readline().split(SEP)
    return quesiti

def MostraQuesito(quesiti:list, numero:int):
     i=0
     while(i<len(quesiti) and quesiti[i][0]!=numero):
         i+=1

     if(i<len(quesiti)):
         print('Quesito',str(quesiti[i][0]))
         print()
         print(' ',quesiti[i][1])
         print()
         for j in range(2,6):
             print(str(chr(95+i))+')', quesiti[i][j])
     else:
        print('Quesito NON Trovato')
     
def QuesitoRandomizzato(quesiti:list, numero:int):
     i=0
     while(i<len(quesiti) and quesiti[i][0]!=numero):
         i+=1

     if(i<len(quesiti)):
         print('Quesito',str(quesiti[i][0]))
         print()
         print(' ',quesiti[i][1])
         print()
         
         items=[]
         for j in range(2,6):
             items.append(quesiti[i][j])

         q=[]
         indici=[0,1,2,3]
         giusta=-1
         while(len(indici)>0):
            i=randint(0,len(indici)-1)
            if(indici[i]==0): giusta=len(q)
            q.append(items[indici[i]])
            x=indici.pop(i)
            
         for i in range(0,len(q)):
            print(str(chr(97+i))+')', q[i])
         return giusta
     else:
        print('Quesito',str(numero) ,' NON Trovato')
        return -1

def Test(quesiti:list, numero:int):
    giusto = QuesitoRandomizzato(quesiti, numero)
    if(giusto==-1): return
    scelta=input('scelta-->')
    cond = scelta not in {'a','b','c','d'}
    while(cond):
        print('SCELTA non Valida')
        scelta=input('scelta-->')
        cond = scelta not in {'a','b','c','d'}
    if( (ord(scelta)-ord('a')) == giusto): 
        print('esatto')
        return OK
    else: 
        print('ERRATO era la:', chr(giusto+ord('a')))
        return ERRATO
    
           
def Corretti(quesiti, inizio, fine, oneByone=True):
    i=0
    while(i<len(quesiti) and quesiti[i][0]<inizio):
         i+=1
     
    while(i<len(quesiti) and quesiti[i][0]<=fine):
         print('Quesito',str(quesiti[i][0]))
         print()
         print(' ',quesiti[i][1])
         print()
         print(quesiti[i][2])
         i+=1
         if(oneByone):
             input('-- premi Invio --')
             print('='*50)
             
def Prova(quesiti, inizio, fine):
    for i in range(inizio, fine+1):
        Test(quesiti,i)

def Studia(area, inizio, fine):
    quesiti = __CaricaArea(area)
    Corretti(quesiti,inizio,fine)
    Prova(quesiti,inizio,fine)

def __provaArea(area, qty):
    quesiti = __CaricaArea(area)

    errati=[]

    for i in range(0, qty):
        x = randint(0, len(quesiti)-1)
        if(not Test(quesiti,quesiti[x][0])):
            errati.append(quesiti[x])
        quesiti.pop(x)

    return errati

def ProvaArea(area, qty):
    errati = __provaArea(area, qty)
    print('='*50)
    print('='*50)
    print("Quesiti errati", len(errati))

    if(len(errati)>0):
        c = input('Vuoi vedere gli errati (s/n) ?')
        if(c=='s'): 
            for q in errati:
                Corretti(errati, q[0],q[0])
            
            print('='*50)
            
    

    

def CercaLeggi(area):
    pass

print('------------------------')
print(' Quiz prova preselettiva')
print('1: __EstraiFile')
print('2: Studia')
print("3: ProvaArea")

