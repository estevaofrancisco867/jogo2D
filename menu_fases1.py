import os
import WConio2
import menu1
import trocar_tela
import sprites

def menu_fases():
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

    #função para desenhar na tela(matriz)
    def DesenharTela(tela, y_nome_fase1, x_nome_fase1, y_primeiro_elemento_imagem_fase1, x_primeiro_elemento_imagem_fase1, y_nome_fase2, x_nome_fase2, y_primeiro_elemento_imagem_fase2, x_primeiro_elemento_imagem_fase2, y_nome_fase3, x_nome_fase3, y_primeiro_elemento_imagem_fase3, x_primeiro_elemento_imagem_fase3, y_seta, x_seta):
        print("A, a, seta esquerda\nD, d, seta direita\nEsc para voltar\nEnter para selecionar")
        for y in range(altura_y):
            for x in range(largura_x):
                #Desenha nome da primeira fase
                if y == y_nome_fase1 and x == x_nome_fase1:
                    tela[y][x] = "V"
                    tela[y][x+1] = "I"
                    tela[y][x+2] = "A"

                    tela[y][x+4] = "L"
                    tela[y][x+5] = "Á"
                    tela[y][x+6] = "C"
                    tela[y][x+7] = "T"
                    tela[y][x+8] = "E"
                    tela[y][x+9] = "A"
                #Desenha a imagem da Via Láctea
                if y == y_primeiro_elemento_imagem_fase1 and x == x_primeiro_elemento_imagem_fase1:
                    linhas = imagem_fase1.splitlines()  #quebra a imagem em linhas e coloca em uma lista
                    for i1, linha in enumerate(linhas):     # i1 = índice da linha
                        for i2, elemento in enumerate(linha):       # i2 = índice do caractere
                            tela[y + i1][x + i2] = elemento     # desenha o elemento

                #Desenha nome da segunda fase
                if y == y_nome_fase2 and x == x_nome_fase2:
                    tela[y][x] = "H"
                    tela[y][x+1] = "O"
                    tela[y][x+2] = "A"
                    tela[y][x+3] = "G"
                    tela[y][x+4] = "'"
                    tela[y][x+5] = "S"
                #Desenha a imagem de Hoag´s
                if y == y_primeiro_elemento_imagem_fase2 and x == x_primeiro_elemento_imagem_fase2:
                    linhas = imagem_fase2.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento


                #Desenha nome da terceira fase
                if y == y_nome_fase3 and x == x_nome_fase3:
                    tela[y][x] = "A"
                    tela[y][x+1] = "N"
                    tela[y][x+2] = "D"
                    tela[y][x+3] = "R"
                    tela[y][x+4] = "Ô"
                    tela[y][x+5] = "M"
                    tela[y][x+6] = "E"
                    tela[y][x+7] = "D"
                    tela[y][x+8] = "A"
                #Desenha a imagem de Andrômeda
                if y == y_primeiro_elemento_imagem_fase3 and x == x_primeiro_elemento_imagem_fase3:
                    linhas = imagem_fase3.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento

                #Desenha seta
                tela[y_seta][x_seta] = ">"
                tela[y_seta][x_seta-1] = "-"


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

    #função para mudar as coordenadas da seta indicadora na tela(matriz)
    def MudaCoordenadaYSetaIndicadora(codigo, x_seta, x_nome_fase1, x_nome_fase3):
        if x_seta > x_nome_fase1 and (codigo == 65 or codigo == 97 or codigo == 75): #(A, a, seta para esquerda)
            x_seta -= 72
        elif x_seta < (x_nome_fase3 - 2) and (codigo == 68 or codigo == 100 or codigo == 77): #(D, d, seta para direita)
            x_seta += 72
        return x_seta


    '''
    ===== FASES =====
    '''

    #== LIMPANDO O TERMINAL ==
    os.system('cls')

    #== CRIANDO TELA ==
    tela = []
    item = " "

    # espeficações tela
    altura_y = 38
    largura_x = 150

    #coordenadas fase 1
    y_nome_fase1 = 7     #coordenada y inicial do primeiro item esquerdo do nome da primeira fase
    x_nome_fase1 = 27
    y_primeiro_elemento_imagem_fase1 = 10     #coordenada y do primeiro elemento da imagem
    x_primeiro_elemento_imagem_fase1 = 5    #coordenada x do primeiro elemento da imagem
    imagem_fase1 = sprites.get_fase1()

    #coordenadas fase2
    y_nome_fase2 = 7
    x_nome_fase2 = 99
    y_primeiro_elemento_imagem_fase2 = 18
    x_primeiro_elemento_imagem_fase2 = 85
    imagem_fase2 = sprites.get_fase2()

    #coordenadas fase3
    y_nome_fase3 = 7
    x_nome_fase3 = 171
    y_primeiro_elemento_imagem_fase3 = 14
    x_primeiro_elemento_imagem_fase3 = 150
    imagem_fase3 = sprites.get_fase3()
    #coordenadas iniciais da Seta Indicadora no menu
    y_seta = 7
    x_seta = 25
    # #estado:opção escolhida
    # state = ""


    # cria a tela
    CriarTela(altura_y, largura_x, tela, item)

    # relogio geral
    cont = 0

    #codigo do input do jogador inicial
    codigo = 0

    while True:
        altura_y = 38
        largura_x = 150

        #== LIMPANDO TELA ==
        LimparTela(tela)

        #== DESENHAR O MENU NA TELA ==
        DesenharTela(tela, y_nome_fase1, x_nome_fase1, y_primeiro_elemento_imagem_fase1, x_primeiro_elemento_imagem_fase1, y_nome_fase2, x_nome_fase2, y_primeiro_elemento_imagem_fase2, x_primeiro_elemento_imagem_fase2, y_nome_fase3, x_nome_fase3, y_primeiro_elemento_imagem_fase3, x_primeiro_elemento_imagem_fase3, y_seta, x_seta)

        #== COLOCANDO A TELA NO TERMINAL ==
        gotoxy(0,0)
        MostrarTela(tela)

        #== RELOGIO AUMENTA ==
        cont = AumentarRelogio(cont)

        #== CAPTURA INPUT DO JOGADOR ==
        codigo = CapturaInput(codigo)

        # se ESC for apertado
        if codigo == 27: 
            menu1.menu()
            break

            # se ENTER for apertado e a seta estiver em Via Láctea
        if codigo == 13 and x_seta == (x_nome_fase1 - 2):
            trocar_tela.trocar_tela("jogo")
            break

        # se ENTER or apertado e a seta estiver em Hoag´s
        if codigo == 13 and x_seta == (x_nome_fase2 - 2):
            trocar_tela.trocar_tela("jogo")
            break

        # se Enter for apertado e a seta estiver em Andrômeda
        if codigo == 13 and x_seta == (x_nome_fase3 - 2):
            trocar_tela.trocar_tela("jogo")
            break

        #== MUDA A POSICAO DA SETA SEGUNDO INPUT ==
        x_seta = MudaCoordenadaYSetaIndicadora(codigo, x_seta, x_nome_fase1, x_nome_fase3)
    #menu()