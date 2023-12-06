import os
import random
from colorama import Fore, Back, Style


jogarNovamente="s"
jogadas=0
quemJoga=2 #1 - cpu ; 2 - pessoa
maxJogadas=9
vit="n"
velha=[
    [" ", " "," "],
    [" ", " "," "],
    [" ", " "," "]
]

def tela():
    global velha
    global jogadas
    os.system("clear")
    print("    0    1    2")
    print("0:  "+ velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2] + " | ")
    print("   -----------")
    print("1:  "+ velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2] + " | ")
    print("   -----------")
    print("2:  "+ velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2] + " | ")
    print("jogadas: "+ Fore.GREEN + str(jogadas) + Fore.RESET)
tela()
def jogadorJoga():
    global jogadas
    global quemJoga
    
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        
        try:
            l=int(input("Linha: "))
            c=int(input("Coluna: "))
        
            while velha[l][c] != " ":
                l=int(input("Linha: "))
                c=int(input("Coluna: "))
            velha[l][c] = "X"
            quemJoga=1
            jogadas+=1
        except:
            print("Jogada Invalida")
            os.system("pause")
            
def cpuJoga():
    global jogadas
    global quemJoga
    
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)

        while velha[l][c] != " ":
                 l=random.randrange(0,3)
                 c=random.randrange(0,3)
        velha[l][c] = "O"
        quemJoga=2
        jogadas+=1

def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos= ["X","O"]
    for c in simbolos:
        vitoria = "n"
        #verifica linha
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic < 3:
                if (velha[il][ic]==c):
                    soma+=1
                ic+=1
            
            if(soma==3):
                vitoria = c
                break
            il+=1
        if(vitoria != "n"):
            break
        #verifica coluna
        il=ic=0
        
        while ic<3:
            soma=0
            il=0
            while il < 3:
                if (velha[il][ic]==c):
                    soma+=1
                il+=1
            
            if(soma==3):
                vitoria = c
                break
            ic+=1
        if(vitoria != "n"):
            break
        
        #verifica diagonal
        soma=0
        idiag= 0
        while idiag<3:
             
            if(velha[idiag][idiag]==c):
                soma+=1
            idiag+=1
            if(soma==3):
                vitoria = c
                break
        if(vitoria != "n"):
          break
        soma=0
        idiagl= 0
        idiagc= 2
        while idiagl<3:
             
            if(velha[idiagl][idiagc]==c):
                soma+=1
            idiagl+=1
            idiagc-=1
            if(soma==3):
                vitoria = c
                break
        if(vitoria != "n"):
          break
    return vitoria
def redefinir():
   
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    global velha
    jogadas=0
    quemJoga=2 #1 - cpu ; 2 - pessoa
    maxJogadas=9
    vit="n"
    velha=[
        [" ", " "," "],
        [" ", " "," "],
        [" ", " "," "]
    ]

               

while(jogarNovamente == "s"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        print("oi")
        if((vit!= "n") or (jogadas>= maxJogadas)):
            break
    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
    if(vit=="X" or vit=="O"):
        print ("Resultado: Jogador "  + vit + "Venceu")
    else: 
        print("Resultado: Empate")
    jogarNovamente=input(Fore.BLUE + "Jogar Novamente? [s/n]" + Fore.RESET)
    redefinir()
