import fitz
import os
from random import randint

SEP = '#'

os.chdir('/home/antonio/Scrivania/Scuola/Scuola_2021-2022/PRESIDI')

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
    #text=text.replace('\n','')
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
    print('Fine Caricamento QUESITI')

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

def MostraQuesito(area, numero):
     f=open('area_'+str(area)+'.csv', 'r')
     l=f.readline().split(SEP)
     while(l[0]!='' and not l[0].endswith(str(area)+'.'+str(numero))):
         l=f.readline().split(SEP)
     if( l[0] !=''):
         print(l[0])
         print()
         print(' ',l[1])
         print()
         for i in range(2,6):
             print(str(chr(95+i))+')', l[i])
     else:
        print('Quesito NON Trovato')
     
def QuesitoRandomizzato(area, numero):
     f=open('area_'+str(area)+'.csv', 'r')
     l=f.readline().split(SEP)
     while(l[0]!='' and not l[0].endswith(str(area)+'.'+str(numero))):
         l=f.readline().split(SEP)
     if( l[0] !=''):
         print(l[0])
         print()
         print(' ',l[1])
         print()
         
         quesiti=[]
         for i in range(2,6):
             quesiti.append(l[i])
             #print(l[i])

         q=[]
         indici=[0,1,2,3]
         giusta=-1
         while(len(indici)>0):
            i=randint(0,len(indici)-1)
            if(indici[i]==0): giusta=len(q)
            q.append(quesiti[indici[i]])
            x=indici.pop(i)
            
         for i in range(0,len(q)):
            print(str(chr(97+i))+')', q[i])
         return giusta
     else:
        print('Quesito',str(numero) ,' NON Trovato')
        return -1

def Test(area, numero):
    giusto = QuesitoRandomizzato(area, numero)
    if(giusto==-1): return
    scelta=input('scelta-->')
    cond = scelta not in {'a','b','c','d'}
    while(cond):
        print('SCELTA non Valida')
        scelta=input('scelta-->')
        cond = scelta not in {'a','b','c','d'}
    if( (ord(scelta)-ord('a')) == giusto): print('esatto')
    else: print('ERRATO era la:', chr(giusto+ord('a')))
    
           
def Corretti(area, inizio, fine, oneByone=True):
    f=open('area_'+str(area)+'.csv', 'r')
    l=f.readline().split(SEP)
    while(l[0]!='' and not l[0].endswith(str(area)+'.'+str(inizio))):
         l=f.readline().split(SEP)
    
    while(l[0]!='' and int(l[0].split('.')[1])<=fine):
         print(l[0])
         print()
         print(' ',l[1])
         print()
         print(l[2])
         l=f.readline().split(SEP)
         if(oneByone):
             input('-- premi Invio --')
             print('='*50)
             
def Prova(area, inizio, fine):
    for i in range(inizio, fine+1):
        Test(area,i)

def Studia(area, inizio, fine):
    Corretti(area,inizio,fine)
    Prova(area,inizio,fine)

def ProvaArea(area, qty):
    c = 0
    quesiti = __CaricaArea(7)

    for i in range(0, qty):
        x = randint(0, len(quesiti)-1)
        Test(area,quesiti[x][0])
        quesiti.pop(x)

def CercaLeggi(area):
    pass


# __EstraiFile()


ProvaArea(7,1)


