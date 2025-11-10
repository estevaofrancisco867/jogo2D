import os
import WConio2
import trocar_tela
import sprites
import status

def menu_melhorias():
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
    def DesenharTela(tela,  y_seta, x_seta):
        for y in range(altura_y):
            for x in range(largura_x):

                #sprite do foguete do menu
                if y == y_foguete and x == x_foguete:
                    for fy, linha in enumerate(sprites.get_foguete_menu()):
                        for fx, caractere in enumerate(linha):
                            if 0 <= y_foguete + fy < len(tela) and 0 <= x_foguete + fx < len(tela[0]): # ve se o sprite ta dentro da tela
                                tela[y_foguete + fy][x_foguete + fx] = caractere

                if y == y_dinheiro and x == x_dinheiro:
                    tela[y][x] = f"{status.moedas}"
                    tela[y][x+1] = "R"
                    tela[y][x+2] = "$"

                #sprites de dano, vida e vel. tiro
                if y == y_dano and x == x_dano:
                    for dy, linha in enumerate(sprites.get_dano()):  
                        for dx, caractere in enumerate(linha):
                            if 0 <= y_dano + dy < len(tela) and 0 <= x_dano + dx < len(tela[0]): # ve se o sprite ta dentro da tela
                                tela[y_dano + dy][x_dano + dx] = caractere

                if y == y_vida and x == x_vida:
                    for vy, linha in enumerate(sprites.get_vida()):  
                        for vx, caractere in enumerate(linha):
                            if 0 <= y_vida + vy < len(tela) and 0 <= x_vida + vx < len(tela[0]): # ve se o sprite ta dentro da tela
                                tela[y_vida + vy][x_vida + vx] = caractere

                if y == y_vel_tiro and x == x_vel_tiro:
                    for vel_y, linha in enumerate(sprites.get_vel_tiro()):  
                        for vel_x, caractere in enumerate(linha):
                            if 0 <= y_vel_tiro + vel_y < len(tela) and 0 <= x_vel_tiro + vel_x < len(tela[0]): # ve se o sprite ta dentro da tela
                                tela[y_vel_tiro + vel_y][x_vel_tiro + vel_x] = caractere
                #Desenha seta
                tela[y_seta][x_seta] = ">"

                #desenha os limites da tela
                tela[y][largura_x - 1] = "*"
                tela[y][0] = "*"
                tela[altura_y - 1][x] = "*"
                tela[0][x] = "*"


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
    def MudaCoordenadaYSetaIndicadora(codigo, y_seta, x_seta, y_vida, y_vel_tiro):
        if y_seta > y_vida and (codigo == 119 or codigo == 87 or codigo == 72):
            y_seta -= 10
        elif y_seta < y_vel_tiro and (codigo == 115 or codigo == 83 or codigo == 80):
            y_seta += 10
        return y_seta

    # def melhorar(moedas,atributo): 
    #     if atributo == status.vida or atributo == status.dano:
    #         match atributo:
    #             case 1:
    #                 if moedas >= 5:
    #                     moedas -= 5
    #                     atributo += 1
    #                     return moedas, atributo
    #             case 2:
    #                 if moedas >= 10:
    #                     moedas -= 10
    #                     atributo += 1
    #                     return moedas, atributo # quebrado (vai ter q separar um pouco isso dai)
    #             case _: return moedas, atributo  
    #     elif atributo == status.lerdeza_tiro:
    #         match atributo:
    #             case 20:
    #                 if moedas >= 5:
    #                     moedas -= 5
    #                     atributo -= 10
    #                     return moedas, atributo
    #             case 10:
    #                 if moedas >= 10:
    #                     moedas -= 5
    #                     atributo -= 10
    #                     return moedas, atributo
    #             case _: return moedas, atributo


    '''
    ===== FASES =====
    '''

    #== LIMPANDO O TERMINAL ==
    os.system('cls')

    #== CRIANDO TELA ==
    tela = []
    item = " "

    # espeficações tela
    altura_y = 40
    largura_x = 200

    #coordenadas iniciais titulo
    y_titulo = 7     #coordenada y inicial do primeiro item esquerdo do nome do jogo
    esquerda_x_titulo = 18     #coordenada x inicial da primeiro item esquerdo do nome do jogo
    #coordenadas iniciais CONTINUAR
    #y_vida = 9
    esquerda_x_continuar = 21
    #coordenadas iniciais NOVO JOGO
    y_novojogo = 11
    esquerda_x_novojogo = 21
    #coordenadas iniciais MELHORIAS
    #y_vel_tiro = 13
    esquerda_x_melhorias = 21
    #coordenadas iniciais da Seta Indicadora no menu
    y_seta = 7
    x_seta = 119
    y_dinheiro, x_dinheiro = [2,largura_x - 10]
    y_vida, x_vida = [5,120] #eh o primeiro caractere de cima 
    y_dano, x_dano = [15, 120]
    y_vel_tiro, x_vel_tiro = [25,120]
    y_foguete, x_foguete = [5, 10]

    lvl_vida,lvl_dano,lvl_vel_tiro = [1,1,1]


    # cria a tela
    CriarTela(altura_y, largura_x, tela, item)

    # relogio geral
    cont = 0

    #codigo do input do jogador inicial
    codigo = 0

    while True:

        #== LIMPANDO TELA ==
        LimparTela(tela)

        #== DESENHAR O MENU NA TELA ==
        DesenharTela(tela, y_seta, x_seta)

        #== COLOCANDO A TELA NO TERMINAL ==
        gotoxy(0,0)
        MostrarTela(tela)

        #== RELOGIO AUMENTA ==
        cont = AumentarRelogio(cont)

        #== CAPTURA INPUT DO JOGADOR ==
        codigo = CapturaInput(codigo)

        if codigo == 27: 
            os.system("cls")
            break
        # se ENTER for apertado e a seta estiver em CONTINUAR
        if codigo == 13 and y_seta == 7:
            # status.moedas, status.vida = melhorar(status.moedas)
            break
        # se ENTER or apertado e a seta estiver em NOVO JOGO
        if codigo == 13 and y_seta == 17:
            break
        if codigo == 13 and y_seta == 27:
            break

        #== MUDA A POSICAO DA SETA SEGUNDO INPUT ==
        y_seta = MudaCoordenadaYSetaIndicadora(codigo, y_seta, x_seta, y_vida, y_vel_tiro)
