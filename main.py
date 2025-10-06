import os
import WConio2 #pip install WConio2
import random

tela = []
cont = 0
largura = 51 #originalmente 50
altura = 45

aviao_y = altura - 1
aviao_x = largura // 2
tiro_y = -1
tiro_x = -1

# Cada inimigo é uma tupla (x, y)
inimigos = [(5, 0), (10, 0), (15, 0),(7, 0), (12, 0), (16, 0)]
acertos = 0

# Criar funcao para tirar o pisca-pisca
def gotoxy(x, y):
    print(f"\033[{y};{x}H", end="", flush=True)

# Limpa o terminal ao executar
def limpar_tela():
    os.system("cls")

# Criando a tela
def criar_tela(altura, largura):
    for y in range(altura):
        tela.append([])
        for x in range(largura):
            tela[y].append("")
    return tela        

def preencher_tela(tela,altura,largura,inimigos):
    for y in range(altura):
        for x in range(largura):
            if (x, y) in inimigos:
                tela[y][x] ="@"
            elif y == tiro_y and x == tiro_x:
                tela[y][x] = "|"
            elif y == aviao_y and x == aviao_x:
                tela[y][x] = "^"
            else:
                tela[y][x] = " "

def mostrar_tela(tela,altura,largura,acertos):
    print("*"*(largura+2))
    for x in range(altura):
        print("*", end='')
        for y in range(largura):
            print(tela[x][y], end = '')
        print("*")
    print("*"*(largura+2))
    print(f"Acertos: {acertos}/50")

def verifica_colisao(tiro_x,tiro_y,inimigos):
    global acertos, tiro_y
    if (tiro_x, tiro_y) in inimigos:
        inimigos.remove((tiro_x, tiro_y))
        acertos += 1
        tiro_y = -1
        print("Acertou!")
        return True
    return False    

def checar_vitoria():
    if acertos >= 50:
        print("Você venceu com 50 acertos!")
        return True
    return False

def checar_derrota():
    if any(y == aviao_y and x == aviao_x for (x, y) in inimigos) or any(y == altura - 1 for (x, y) in inimigos):
        print("Você foi atingido! Game Over.")
        return True
    return False

def entrada_jogador():
    global aviao_x, aviao_y, tiro_x, tiro_y
    print("a=esq d=dir w=cima s=baixo f=fogo: ")
    if WConio2.kbhit():
        codigo, simbolo = WConio2.getch()

        match codigo:
            case 97: 
                if aviao_x > 0:
                    aviao_x -= 1
            case 100:
                if aviao_x < largura - 1:
                    aviao_x += 1
            case 119:
                if aviao_y > 0:
                    aviao_y -= 1
            case 115:
                if aviao_y < altura - 1:
                    aviao_y += 1
            case 102: 
                if tiro_y == -1:
                    tiro_x = aviao_x
                    tiro_y = aviao_y

def movertiro(tiro_y):
    if tiro_y >= 0:
        return tiro_y - 1
    return tiro_y     

def moverInimigos(cont,inimigos,altura):
    if cont % 100 == 0:
        return [(x, y + 1) for (x, y) in inimigos if y + 1 < altura]
    return inimigos

def novos_inimigos(inimigos):
    if inimigos == []:
       return[(3, 0),(17, 0),(20, 0),(22, 0)]
    return inimigos



limpar_tela()
criar_tela(altura, largura)

while True:
    cont += 1
    gotoxy(0,0)

    entrada_jogador()
    tiro_y = movertiro(tiro_y)
    verifica_colisao(tiro_x,tiro_y,inimigos)

    inimigos = moverInimigos(cont,inimigos,altura)
    inimigos = novos_inimigos(inimigos)

    preencher_tela(tela,altura,largura,inimigos)
    mostrar_tela(tela,altura,largura,acertos)

    if checar_vitoria() or checar_derrota():
        break
