import os
import WConio2


#função para mudar o local do cursor
def gotoxy(x, y):
    print(f"\033[{y};{x}H", end='', flush=True)

#função para criar tela(matriz)
def CriarTela(altura_y, largura_x, tela, item):
    for y in range(altura_y):
        tela.append([])
        for x in range(largura_x):
            tela[y].append(item)

#função para limpar a tela(matriz)
def LimparTela(tela):
    for y in range(altura_y):  #vertical        
        for x in range(largura_x): #horizontal
            tela[y][x] = " "

#função para mudar as coordenadas da seta indicadora na tela(matriz)
def CalculaCoordenadasSetaIndicadora(codigo, y_seta, y_continuar):
    #Calculo para ver onde fica a seta indicadora segundo input do jogador
    if codigo == 115 or codigo == 83 or codigo == 80 and y_seta < y_melhorias: #(s, S, seta para baixo)
        y_seta += 2
    elif codigo == 119 or codigo == 87 or codigo == 72 and y_seta > y_continuar: #(w, W, seta para cima)
        y_seta -= 2
    return y_seta

#função para desenhar na tela(matriz)
def DesenharTela(tela, y_titulo, esquerda_x_titulo, y_continuar, esquerda_x_continuar, y_novojogo, esquerda_x_novojogo, y_melhorias, esquerda_x_melhorias, codigo, y_seta, x_seta):
    for y in range(altura_y):
        for x in range(largura_x):
            #Desenha titulo
            if y == y_titulo and x == esquerda_x_titulo:
                tela[y][x] = "S"
                tela[y][x+1] = "P"
                tela[y][x+2] = "A"
                tela[y][x+3] = "C"
                tela[y][x+4] = "E"

                tela[y][x+6] = "I"
                tela[y][x+7] = "N"
                tela[y][x+8] = "V"
                tela[y][x+9] = "A"
                tela[y][x+10] = "D"
                tela[y][x+11] = "E"
                tela[y][x+12] = "R"
                tela[y][x+13] = "S"

            #Desenha continuar
            if y == y_continuar and x == esquerda_x_continuar:
                tela[y][x] = "C"
                tela[y][x+1] = "O"
                tela[y][x+2] = "N"
                tela[y][x+3] = "T"
                tela[y][x+4] = "I"
                tela[y][x+5] = "N"
                tela[y][x+6] = "U"
                tela[y][x+7] = "A"
                tela[y][x+8] = "R"

            #Desenha novo jogo
            if y == y_novojogo and x == esquerda_x_novojogo:
                tela[y][x] = "N"
                tela[y][x+1] = "O"
                tela[y][x+2] = "V"
                tela[y][x+3] = "O"

                tela[y][x+5] = "J"
                tela[y][x+6] = "O"
                tela[y][x+7] = "G"
                tela[y][x+8] = "O"
            
            #Desenha melhorias
            if y == y_melhorias and x == esquerda_x_melhorias:
                tela[y][x] = "M"
                tela[y][x+1] = "E"
                tela[y][x+2] = "L"
                tela[y][x+3] = "H"
                tela[y][x+4] = "O"
                tela[y][x+5] = "R"
                tela[y][x+6] = "I"
                tela[y][x+7] = "A"
                tela[y][x+8] = "S"

            #Desenha Seta indicadora
            tela[y_seta][x_seta] = ">"

#função para colocar a tela(matriz) no terminal
def MostrarTela(tela):
    for y in range(altura_y):
        for x in range(largura_x):
            print(tela[y][x], end='')
        print()     #necessário para separar as listas da coordenada y

#função que aumenta o relogio geral
def AumentarRelogio(cont):
    cont += 1
    return cont

#função para capturar o input do jogador para o menu
def CapturaInput(codigo, cont2):
    if WConio2.kbhit():
        codigo, simbolo = WConio2.getch()
        cont2 += 1
    return codigo, cont2

def DetectaInteracaoJogadorComWConio2(cont2, codigo, y_seta, y_continuar):
        #coordenadas da seta indicadora depois da primeira interação do jogador com o menu
        if cont2 > 0:
            y_seta = CalculaCoordenadasSetaIndicadora(codigo, y_seta, y_continuar)
        return y_seta

'''
===== FASES =====
'''


#== LIMPANDO O TERMINAL ==
os.system('cls')

#== CRIANDO TELA ==
tela = []
item = " "

# espeficações tela
altura_y = 35
largura_x = 50

# cria a tela
CriarTela(altura_y, largura_x, tela, item)

# relogio geral
cont = 0

#coordenadas iniciais título
y_titulo = 7               #coordenada y inicial do nome do jogo
esquerda_x_titulo = 18     #coordenada x inicial da primeiro charactere esquerdo do nome do jogo
#coordenadas iniciais CONTINUAR
y_continuar = 9
esquerda_x_continuar = 21
#coordenadas iniciais NOVO JOGO
y_novojogo = 11
esquerda_x_novojogo = 21
#coordenadas iniciais MELHORIAS
y_melhorias = 13
esquerda_x_melhorias = 21
#coordenadas iniciais para a seta indicadora do menu
y_seta = 9
x_seta = 19

#codigo do input do jogador inicial
codigo = 0
# contador do input
cont2 = 0

while True:
    altura_y = 35
    largura_x = 50

    #== DETECTADOR se o jogador interagiu com o menu através de WConio2 ==
        #-- e define a coordenada y da seta se verdadeiro --
    y_seta = DetectaInteracaoJogadorComWConio2(cont2, codigo, y_seta, y_continuar)

    #== LIMPANDO TELA ==
    LimparTela(tela)


    #== DESENHAR O MENU NA TELA ==
    DesenharTela(tela, y_titulo, esquerda_x_titulo, y_continuar, esquerda_x_continuar, y_novojogo, esquerda_x_novojogo, y_melhorias, esquerda_x_melhorias, codigo, y_seta, x_seta)

    #== Limpa o codigo capturado anteriormente ==
    codigo = 0

    #== COLOCANDO A TELA NO TERMINAL ==
    gotoxy(0,0)
    MostrarTela(tela)

    #== RELOGIO AUMENTA ==
    cont = AumentarRelogio(cont)

    #== CAPTURA INPUT DO JOGADOR ==
    codigo, cont2 = CapturaInput(codigo, cont2)