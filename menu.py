import os
import WConio2 # pip install WConio2
import sprites
import trocar_tela
import salvar

def menu():

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
    def DesenharTela(tela, y_titulo, esquerda_x_titulo, y_continuar, esquerda_x_continuar, y_novojogo, esquerda_x_novojogo, y_melhorias, esquerda_x_melhorias, y_seta, x_seta):
        for y in range(altura_y):
            for x in range(largura_x):
                #Desenha titulo
                if y == y_titulo and x == esquerda_x_titulo:
                    linhas = imagemtitulo.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento

                #Desenha continuar
                if y == y_continuar and x == esquerda_x_continuar:
                    linhas = imagemcontinuar.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento

                #Desenha novo jogo
                if y == y_novojogo and x == esquerda_x_novojogo:
                    linhas = imagemnovojogo.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento
            
                #Desenha melhorias
                if y == y_melhorias and x == esquerda_x_melhorias:
                    linhas = imagemmelhorias.splitlines()
                    for i1, linha in enumerate(linhas):
                        for i2, elemento in enumerate(linha):
                            tela[y + i1][x + i2] = elemento
            
                #Desenhar salvar
                if y == y_salvar and x == esquerda_x_salvar:
                    linhas = imagemsalvar.splitlines()
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
    def MudaCoordenadaYSetaIndicadora(codigo, y_seta, x_seta, y_continuar, y_melhorias):
        if y_seta > y_continuar and (codigo == 119 or codigo == 87 or codigo == 72):
            y_seta -= 5
        elif y_seta < y_salvar and (codigo == 115 or codigo == 83 or codigo == 80):
            y_seta += 5
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
    altura_y = 38
    largura_x = 150

    #coordenadas iniciais titulo
    y_titulo = 1     #coordenada y inicial do primeiro item esquerdo do nome do jogo
    esquerda_x_titulo = 35     #coordenada x inicial da primeiro item esquerdo do nome do jogo
    imagemtitulo = sprites.get_titulo()
    #coordenadas iniciais CONTINUAR
    y_continuar = 18
    esquerda_x_continuar = 52
    imagemcontinuar = sprites.get_continuar()
    #coordenadas iniciais NOVO JOGO
    y_novojogo = 23
    esquerda_x_novojogo = 52
    imagemnovojogo = sprites.get_novojogo()
    #coordenadas iniciais MELHORIAS
    y_melhorias = 28
    esquerda_x_melhorias = 52
    imagemmelhorias = sprites.get_melhorias()
    #coordenadas iniciais SALVAR
    y_salvar = 33
    esquerda_x_salvar = 52
    imagemsalvar = sprites.get_salvar()
    #coordenadas iniciais da Seta Indicadora no menu
    y_seta = 18
    x_seta = 44
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
        DesenharTela(tela, y_titulo, esquerda_x_titulo, y_continuar, esquerda_x_continuar, y_novojogo, esquerda_x_novojogo, y_melhorias, esquerda_x_melhorias, y_seta, x_seta)

        #== COLOCANDO A TELA NO TERMINAL ==
        gotoxy(0,0)
        MostrarTela(tela)

        #== RELOGIO AUMENTA ==
        cont = AumentarRelogio(cont)

        #== CAPTURA INPUT DO JOGADOR ==
        codigo = CapturaInput(codigo)

        # se ESC for apertado
        if codigo == 27: 
            os.system("cls")
            break

        # se ENTER for apertado e a seta estiver em CONTINUAR
        if codigo == 13 and y_seta == y_continuar:
            salvar.carregar()
            trocar_tela.trocar_tela("menu_fases")
            break

        # se ENTER or apertado e a seta estiver em NOVO JOGO
        if codigo == 13 and y_seta == y_novojogo:
            salvar.novo_jogo()
            trocar_tela.trocar_tela("menu_fases")
            break
        # se ENTER or apertado e a seta estiver em MELHORIAS
        if codigo == 13 and y_seta == y_melhorias:
            trocar_tela.trocar_tela("menu_melhorias")
            break
        # se ENTER or apertado e a seta estiver em SALVAR
        if codigo == 13 and y_seta == y_salvar:
            salvar.salvar()

        #== MUDA A POSICAO DA SETA SEGUNDO INPUT ==
        y_seta = MudaCoordenadaYSetaIndicadora(codigo, y_seta, x_seta, y_continuar, y_melhorias)
