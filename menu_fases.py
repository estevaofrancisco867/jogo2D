import os
import WConio2 # pip install WConio2
import trocar_tela
import sprites
import status

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
    def DesenharTela(tela, y_nome_fase1, x_nome_fase1, y_primeiro_elemento_imagem_fase1, x_primeiro_elemento_imagem_fase1,
                      y_nome_fase2, x_nome_fase2, y_primeiro_elemento_imagem_fase2, x_primeiro_elemento_imagem_fase2, y_nome_fase3,
                        x_nome_fase3, y_primeiro_elemento_imagem_fase3, x_primeiro_elemento_imagem_fase3, y_seta, x_seta):
        print("A, a, seta esquerda\tD, d, seta direita\nEsc para voltar\t\tEnter para selecionar")
        for y in range(altura_y):
            for x in range(largura_x):

                #Desenha nome da primeira fase
                if y == y_nome_fase1 and x == x_nome_fase1:
                    linhas = imagem_fase1nome.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento

                #Desenha a imagem da Via Láctea
                if y == y_primeiro_elemento_imagem_fase1 and x == x_primeiro_elemento_imagem_fase1:
                    linhas = imagem_fase1.splitlines()  #quebra a imagem em linhas e coloca em uma lista
                    for i1, linha in enumerate(linhas):     # i1 = índice da linha
                        for i2, elemento in enumerate(linha):       # i2 = índice do caractere
                            tela[y + i1][x + i2] = elemento     # desenha o elemento

                #Desenha nome da segunda fase
                if y == y_nome_fase2 and x == x_nome_fase2:
                    linhas = imagem_fase2nome.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento
                #Desenha a imagem de Hoag´s
                if y == y_primeiro_elemento_imagem_fase2 and x == x_primeiro_elemento_imagem_fase2:
                    linhas = imagem_fase2.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento


                #Desenha nome da terceira fase
                if y == y_nome_fase3 and x == x_nome_fase3:
                    linhas = imagem_fase3nome.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento
                #Desenha a imagem de Andrômeda
                if y == y_primeiro_elemento_imagem_fase3 and x == x_primeiro_elemento_imagem_fase3:
                    linhas = imagem_fase3.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento

                #Desenha seta
                if y == y_seta and x == x_seta:
                    linhas = imagemseta.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento



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
            x_seta -= 50
        elif x_seta < (x_nome_fase3 - 7) and (codigo == 68 or codigo == 100 or codigo == 77): #(D, d, seta para direita)
            x_seta += 50
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
    y_nome_fase1 = 4     #coordenada y inicial do primeiro item esquerdo do nome da primeira fase
    x_nome_fase1 = 8
    y_primeiro_elemento_imagem_fase1 = 10     #coordenada y do primeiro elemento da imagem
    x_primeiro_elemento_imagem_fase1 = 0    #coordenada x do primeiro elemento da imagem
    imagem_fase1nome = sprites.get_fase1nome()
    imagem_fase1 = sprites.get_fase1()

    #coordenadas fase2
    y_nome_fase2 = 4
    x_nome_fase2 = 58
    y_primeiro_elemento_imagem_fase2 = 18
    x_primeiro_elemento_imagem_fase2 = 56
    imagem_fase2nome = sprites.get_fase2nome()
    imagem_fase2 = sprites.get_fase2()

    #coordenadas fase3
    y_nome_fase3 = 4
    x_nome_fase3 = 108
    y_primeiro_elemento_imagem_fase3 = 14
    x_primeiro_elemento_imagem_fase3 = 96
    imagem_fase3nome = sprites.get_fase3nome()
    imagem_fase3 = sprites.get_fase3()

    #coordenadas iniciais da Seta Indicadora no menu
    y_seta = 4
    x_seta = 1
    imagemseta = sprites.get_seta()

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
        DesenharTela(tela, y_nome_fase1, x_nome_fase1, y_primeiro_elemento_imagem_fase1, x_primeiro_elemento_imagem_fase1,
                      y_nome_fase2, x_nome_fase2, y_primeiro_elemento_imagem_fase2, x_primeiro_elemento_imagem_fase2, y_nome_fase3,
                        x_nome_fase3, y_primeiro_elemento_imagem_fase3, x_primeiro_elemento_imagem_fase3, y_seta, x_seta)

        #== COLOCANDO A TELA NO TERMINAL ==
        gotoxy(0,0)
        MostrarTela(tela)

        #== RELOGIO AUMENTA ==
        cont = AumentarRelogio(cont)

        #== CAPTURA INPUT DO JOGADOR ==
        codigo = CapturaInput(codigo)

        # se ESC for apertado
        if codigo == 27: 
            trocar_tela.trocar_tela("menu")
            break

            # se ENTER for apertado e a seta estiver na Via Láctea
        if codigo == 13 and x_seta == (x_nome_fase1 - 7) and status.fase == 1:
            trocar_tela.trocar_tela("jogo")
            break

        # se ENTER for apertado e a seta estiver em Hoag´s
        elif codigo == 13 and x_seta == (x_nome_fase2 - 7) and status.fase == 2:
            trocar_tela.trocar_tela("jogo")
            break

        # se Enter for apertado e a seta estiver em Andrômeda
        elif codigo == 13 and x_seta == (x_nome_fase3 - 7) and status.fase == 3:
            trocar_tela.trocar_tela("jogo")
            break

        #== MUDA A POSICAO DA SETA SEGUNDO INPUT ==
        x_seta = MudaCoordenadaYSetaIndicadora(codigo, x_seta, x_nome_fase1, x_nome_fase3)