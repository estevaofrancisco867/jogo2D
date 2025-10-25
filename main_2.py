import os
import WConio2  # pip install WConio2
import random

tela = []
cont = 0
largura = 50
altura = 45

aviao_y = altura - 1
aviao_x = largura // 2
tiro_y = -1
tiro_x = -1
powerup_y = -1
powerup_x = -1

# Cada inimigo é uma tupla (x, y)
inimigos = [(5, 0), (10, 0), (15, 0), (7, 0), (12, 0), (16, 0)]
inimigos_horizontais = [(0, 5), (3, 8), (6, 10), (10, 12)]  # agora 4 aviões
direcao_horizontais = [1, 1, 1, 1]  # direção inicial de todos

tiros_inimigos = []  # tiros inimigos
acertos = 0

# Criar função para tirar o pisca-pisca
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

# Renderiza os elementos da tela
def preencher_tela(tela, altura, largura, inimigos):
    for y in range(altura):
        for x in range(largura):
            if (x, y) in inimigos:
                tela[y][x] = "@"
            elif (x, y) in inimigos_horizontais:
                tela[y][x] = "&"
            elif (x, y) in tiros_inimigos:
                tela[y][x] = "!"
            elif y == tiro_y and x == tiro_x:
                tela[y][x] = "|"
            elif y == aviao_y and x == aviao_x:
                tela[y][x] = "^"
            elif y == powerup_y and x == powerup_x:
                tela[y][x] = "P"
            else:
                tela[y][x] = " "

# Mostra a tela, suas bordas * e os acertos
def mostrar_tela(tela, altura, largura, acertos):
    print("*" * (largura + 2))
    for x in range(altura):
        print("*", end='')
        for y in range(largura):
            print(tela[x][y], end='')
        print("*")
    print("*" * (largura + 2))
    print(f"Acertos: {acertos}/50")

# Retorna True caso o tiro acerte em um inimigo
def verifica_colisao(tiro_x, tiro_y, inimigos, inimigos_horizontais):
    global acertos, powerup_x, powerup_y
    if (tiro_x, tiro_y) in inimigos:
        inimigos.remove((tiro_x, tiro_y))
        powerup_x, powerup_y = powerup(powerup_x, powerup_y)
        acertos += 1
        tiro_y = -1
    elif (tiro_x, tiro_y) in inimigos_horizontais :
        inimigos_horizontais.remove((tiro_x, tiro_y))
        powerup_x, powerup_y = powerup(powerup_x, powerup_y)
        acertos += 1
        tiro_y = -1            


def verifica_coleta(powerup_x, powerup_y):
    if powerup_x == aviao_x and powerup_y == aviao_y:
        return -1, -1
    return powerup_x, powerup_y

def powerup(x, y):
    x, y = tiro_x, tiro_y
    return x, y

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
    global aviao_x, aviao_y, tiro_x, tiro_y, altura, largura
    print(f"a,→ d,← w,↑ s,↓ f=fogo.")
    if WConio2.kbhit():
        codigo, simbolo = WConio2.getch()
        print(codigo, " ", simbolo)  # descobre o codigo da tecla pressionada

        def aviao_esquerda(aviao_x):
            if aviao_x > 0:
                return aviao_x - 1
            else:
                return aviao_x

        def aviao_direita(aviao_x, largura):
            if aviao_x < largura - 1:
                return aviao_x + 1
            else:
                return aviao_x

        def aviao_cima(aviao_y):
            if aviao_y > 0:
                return aviao_y - 1
            else:
                return aviao_y

        def aviao_baixo(aviao_y, altura):
            if aviao_y < altura - 1:
                return aviao_y + 1
            else:
                return aviao_y

        def atirar(tiro_x, tiro_y):
            if tiro_y == -1:
                tiro_x = aviao_x
                tiro_y = aviao_y
            return tiro_x, tiro_y

        match codigo:
            case 97: aviao_x = aviao_esquerda(aviao_x)  # a
            case 65: aviao_x = aviao_esquerda(aviao_x)  # A
            case 75: aviao_x = aviao_esquerda(aviao_x)  # → 
            case 100: aviao_x = aviao_direita(aviao_x, largura)
            case 68: aviao_x = aviao_direita(aviao_x, largura)
            case 77: aviao_x = aviao_direita(aviao_x, largura)
            case 119: aviao_y = aviao_cima(aviao_y)
            case 87: aviao_y = aviao_cima(aviao_y)
            case 72: aviao_y = aviao_cima(aviao_y)
            case 115: aviao_y = aviao_baixo(aviao_y, altura)
            case 83: aviao_y = aviao_baixo(aviao_y, altura)
            case 80: aviao_y = aviao_baixo(aviao_y, altura)
            case 102: tiro_x, tiro_y = atirar(tiro_x, tiro_y)  # f
            case 32: tiro_x, tiro_y = atirar(tiro_x, tiro_y)  # espaço

def mover(x, y, intervalo=1, condicao=True, direcao=1):
    if y is not False and x is not False:
        if cont % intervalo == 0:
            if condicao:
                return x + direcao, y + direcao
        return x, y
    if x is not False:
        if cont % intervalo == 0:
            if condicao:
                return x + direcao
        return x
    if y is not False:
        if cont % intervalo == 0:
            if condicao:
                return y + direcao
        return y

def movertiro(tiro_y):
    if tiro_y >= 0:
        return tiro_y - 1
    return tiro_y     

def mover_inimigos(cont, inimigos):
    if cont % 100 == 0:
        return [(x, y + 1) for (x, y) in inimigos if y + 1 < altura]
    return inimigos

def novos_inimigos(inimigos, inimigos_horizontais):
    # Recriar inimigos verticais se todos forem destruídos
    if inimigos == []:
        inimigos = [(3, 0), (17, 0), (20, 0), (22, 0), (25, 0)]
    
    # Recriar inimigos horizontais se todos forem destruídos
    if inimigos_horizontais == []:
        inimigos_horizontais = [(0, 5), (3, 8), (6, 10), (10, 12), (14, 14)]
    
    return inimigos, inimigos_horizontais



# Mover inimigos horizontais
def mover_inimigos_horizontais(cont):
    global inimigos_horizontais, direcao_horizontais
    VELOCIDADE_HORIZONTAL = 50  # Quanto maior, mais lento

    if cont % VELOCIDADE_HORIZONTAL != 0:
        return  # Só move a cada 200 ciclos

    for i in range(len(inimigos_horizontais)):
        x, y = inimigos_horizontais[i]
        direcao = direcao_horizontais[i]

        # Inverter direção se chegar nas bordas
        if x + direcao >= largura - 1 or x + direcao <= 0:
            direcao_horizontais[i] *= -1
            direcao = direcao_horizontais[i]

        inimigos_horizontais[i] = (x + direcao, y)

# Inimigos atiram
def inimigos_atiram():
    global tiros_inimigos
    if cont % 1000 == 0:  # Cada ciclos os inimigos atiram
        for (x, y) in inimigos_horizontais:
            tiros_inimigos.append((x, y + 1))  # Tiros dos inimigos (para baixo)

# Mover tiros dos inimigos
def mover_tiros_inimigos():
    global tiros_inimigos
    VELOCIDADE_TIRO_INIMIGO = 40  # Quanto maior, mais lento

    if cont % VELOCIDADE_TIRO_INIMIGO != 0:
        return  # só move os tiros de vez em quando

    novos_tiros = []
    for (x, y) in tiros_inimigos:
        if y < altura - 1:
            novos_tiros.append((x, y + 1))  # move para baixo
    tiros_inimigos[:] = novos_tiros

# Verificar colisão do tiro inimigo com o avião
def verifica_colisao_tiro_inimigo():
    global acertos
    if (aviao_x, aviao_y) in tiros_inimigos:
        print("Você foi atingido por um tiro inimigo! Game Over.")
        return True  # Retorna True se o avião for atingido
    return False

limpar_tela()
criar_tela(altura, largura)

while True:
    cont += 1
    entrada_jogador()

    gotoxy(0, 0)

    # Mover o tiro do jogador
    tiro_y = mover(False, tiro_y, 1, tiro_y >= 0, -1)

    # Verifica colisão do tiro do jogador com inimigos verticais
    verifica_colisao(tiro_x, tiro_y, inimigos,inimigos_horizontais)
    
   

    # Mover power-up
    powerup_y = mover(False, powerup_y, 20, powerup_y != -1)
    powerup_x, powerup_y = verifica_coleta(powerup_x, powerup_y)

    # Mover inimigos verticais
    inimigos = mover_inimigos(cont, inimigos)

    # Recria inimigos verticais se forem todos destruídos
    inimigos, inimigos_horizontais = novos_inimigos(inimigos, inimigos_horizontais)


    # Mover inimigos horizontais
    mover_inimigos_horizontais(cont)

    # Inimigos horizontais atiram
    inimigos_atiram()

    # Mover os tiros dos inimigos
    mover_tiros_inimigos()

   

    # Preencher e mostrar a tela
    preencher_tela(tela, altura, largura, inimigos)
    mostrar_tela(tela, altura, largura, acertos)

    # Verifica vitória
    if checar_vitoria():
        break
        
     # Verificar se o jogador foi atingido
    if verifica_colisao_tiro_inimigo():
        break  # Se o jogador for atingido, termina o jogo    

    # Verifica derrota por colisão com inimigo vertical
    if checar_derrota():
        break

