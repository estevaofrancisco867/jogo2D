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
def SalvaCoordenadaAtualSetaIndicadora(codigo, y_seta_inicial, x_seta_inicial, y_seta_atual, x_seta_atual):
    for y in range(altura_y):
        for x in range(largura_x):
            #Desenha Seta indicadora na primeira vez sem input do jogador
            if y == y_seta_inicial and x == x_seta_inicial and codigo == None:
                y_seta_atual = y_seta_inicial
                x_seta_atual = x_seta_inicial
            #Desenha Seta indicadora depois do input do jogador
            elif y == y_seta_inicial and x == x_seta_inicial and (codigo == 115 or codigo == 83 or codigo == 80): #se a seta estiver em CONTINUAR e código é: (s, S, seta para baixo)
                y_seta_atual = 11
                x_seta_atual = 19
            elif y == y_seta_inicial and x == x_seta_inicial and (codigo == 119 or codigo == 87 or codigo == 72): #se a seta estiver em CONTINUAR e código é: (w, W, seta para cima)
                y_seta_atual = 9
                x_seta_atual = 19

            return y_seta_atual, x_seta_atual


#função para desenhar na tela(matriz)
def DesenharTela(tela, codigo):
    #coordenadas iniciais titulo
    esquerda_y_titulo = 7     #coordenada y inicial do primeiro item esquerdo do nome do jogo
    esquerda_x_titulo = 18     #coordenada x inicial da primeiro item esquerdo do nome do jogo
    #coordenadas iniciais da Seta Indicadora no menu
    y_seta_inicial = 9
    x_seta_inicial = 19
    #coordenadas atuais da Seta Indicadora após input de jogador
    y_seta_atual = 2
    x_seta_atual = 3
    #coordenadas iniciais CONTINUAR
    esquerda_y_continuar = 9
    esquerda_x_continuar = 21
    #coordenadas iniciais NOVO JOGO
    esquerda_y_novojogo = 11
    esquerda_x_novojogo = 21
    #coordenadas iniciais MELHORIAS
    esquerda_y_melhorias = 13
    esquerda_x_melhorias = 21
    for y in range(altura_y):
        for x in range(largura_x):
            #Desenha titulo
            if y == esquerda_y_titulo and x == esquerda_x_titulo:
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
           
            #Desenha Seta indicadora e salva as coordenadas atuais da seta indicadora

            #Desenha Seta indicadora na primeira vez sem input do jogador
            if y == y_seta_inicial and x == x_seta_inicial and codigo == None:
                tela[y][x] = ">"
                y_seta_atual, x_seta_atual = SalvaCoordenadaAtualSetaIndicadora(codigo, y_seta_inicial, x_seta_inicial, y_seta_atual, x_seta_atual)
            #Desenha Seta indicadora depois do input do jogador
            elif y == y_seta_inicial and x == x_seta_inicial and (codigo == 115 or codigo == 83 or codigo == 80): #se a seta estiver em CONTINUAR e código é: (s, S, seta para baixo)
                # desenha a seta indicadora para NOVO JOGO
                tela[11][19] = ">"
                y_seta_atual, x_seta_atual = SalvaCoordenadaAtualSetaIndicadora(codigo, y_seta_inicial, x_seta_inicial, y_seta_atual, x_seta_atual)
            elif y == y_seta_inicial and x == x_seta_inicial and (codigo == 119 or codigo == 87 or codigo == 72): #se a seta estiver em CONTINUAR e código é: (w, W, seta para cima)
                # desenha a seta indicadora para CONTINUAR
                tela[9][19] = ">"
                y_seta_atual, x_seta_atual = SalvaCoordenadaAtualSetaIndicadora(codigo, y_seta_inicial, x_seta_inicial, y_seta_atual, x_seta_atual)


            #Desenha continuar
            if y == esquerda_y_continuar and x == esquerda_x_continuar:
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
            if y == esquerda_y_novojogo and x == esquerda_x_novojogo:
                tela[y][x] = "N"
                tela[y][x+1] = "O"
                tela[y][x+2] = "V"
                tela[y][x+3] = "O"

                tela[y][x+5] = "J"
                tela[y][x+6] = "O"
                tela[y][x+7] = "G"
                tela[y][x+8] = "O"
            
            #Desenha melhorias
            if y == esquerda_y_melhorias and x == esquerda_x_melhorias:
                tela[y][x] = "M"
                tela[y][x+1] = "E"
                tela[y][x+2] = "L"
                tela[y][x+3] = "H"
                tela[y][x+4] = "O"
                tela[y][x+5] = "R"
                tela[y][x+6] = "I"
                tela[y][x+7] = "A"
                tela[y][x+8] = "S"


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
def CapturaInput(codigo):
    if WConio2.kbhit():
        codigo, simbolo = WConio2.getch()
        return codigo

'''
        if codigo == 97 or codigo == 65 or codigo == 75: #(a, A, seta para esquerda)
        if codigo == 115 or codigo == 83 or codigo == 80: #(s, S, seta para baixo)
        if codigo == 100 or codigo == 68 or codigo == 77: #(d, D, seta para direita)
        if codigo == 119 or codigo == 87 or codigo == 72: #(w, W, seta para cima)'''


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

#codigo do input do jogador inicial
codigo = None

while True:
    altura_y = 35
    largura_x = 50


    #== LIMPANDO TELA ==
    LimparTela(tela)


    #== DESENHAR O MENU NA TELA ==
    DesenharTela(tela, codigo)


    #== COLOCANDO A TELA NO TERMINAL ==
    gotoxy(0,0)
    MostrarTela(tela)

    #== RELOGIO AUMENTA ==
    cont = AumentarRelogio(cont)

    #== CAPTURA INPUT DO JOGADOR ==
    codigo = CapturaInput(codigo)

print(x_seta_atual, " ", y_seta_atual)