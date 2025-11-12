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

                #sprite do foguete do menu e do dinheiro
                if y == y_foguete and x == x_foguete:
                    mostrar_sprite(sprites.get_foguete_menu(),x_foguete,y_foguete)

                if y == y_dinheiro and x == x_dinheiro:
                    mostrar_sprite(sprites.get_dinheiro_menu(status.moedas),x_dinheiro,y_dinheiro)
                #sprites de dano, vida e vel. tiro
                if y == y_dano and x == x_dano:
                    mostrar_sprite(sprites.get_dano(dano),x_dano,y_dano)

                if y == y_vida and x == x_vida:
                    mostrar_sprite(sprites.get_vida(vida),x_vida,y_vida)

                if y == y_vel_tiro and x == x_vel_tiro:
                    mostrar_sprite(sprites.get_vel_tiro(vel_tiro),x_vel_tiro,y_vel_tiro)

                if y == y_voltar and x == x_voltar:
                    mostrar_sprite(sprites.get_voltar(),x_voltar,y_voltar)
                #Desenha seta
                if y == y_seta and x == x_seta:
                    mostrar_sprite(sprites.get_seta(),x_seta,y_seta)

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

    def mostrar_sprite(sprite,sprite_x,sprite_y):
        nonlocal tela
        for y, linha in enumerate(sprite):
            for x, caractere in enumerate(linha):
                    tela[y + sprite_y][x + sprite_x] = caractere

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
    def MudaCoordenadaYSetaIndicadora(codigo, y_seta, y_vida, y_voltar):
        if y_seta > y_vida + 1 and (codigo == 119 or codigo == 87 or codigo == 72):
            if y_seta == y_voltar:
                y_seta -= 7
            else:
                y_seta -= 10
        elif y_seta + 1 <= y_voltar and (codigo == 115 or codigo == 83 or codigo == 80):
            if y_seta == y_voltar - 7:
                y_seta += 7
            else:
                y_seta += 10
        return y_seta

    #as funções melhorar pegam o status e passam para o próximo nivel se tiver dinheiro suficiente
    def melhorar_vida(moedas):
        custo = 0
        valor = vida
        if valor == vida_lvl[1]: custo = custo_upg_1
        elif valor == vida_lvl[2]: custo = custo_upg_2
        elif valor == vida_lvl[3]: return moedas, valor
        if moedas > custo:
            moedas -= custo
            valor += 1
        return moedas,valor
    
    def melhorar_dano(moedas):
        custo = 0
        valor = dano
        if valor == dano_lvl[1]: custo = custo_upg_1
        elif valor == dano_lvl[2]: custo = custo_upg_2
        elif valor == dano_lvl[3]: return moedas, valor
        if moedas > custo:
            moedas -= custo
            valor += 1
        return moedas,valor
    
    def melhorar_vel_tiro(moedas):
        custo = 0
        valor = vel_tiro
        if valor == vel_tiro_lvl[1]: custo = custo_upg_1
        elif valor == vel_tiro_lvl[2]: custo = custo_upg_2
        elif valor == vel_tiro_lvl[3]: return moedas, valor
        if moedas > custo:
            moedas -= custo
            valor -= 6
            print(valor)
        return moedas,valor
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

    #coordenadas iniciais
    y_seta = 6
    x_seta = 57
    y_dinheiro, x_dinheiro = [2,largura_x - 30]
    y_vida, x_vida = [5,60] #eh o primeiro caractere de cima 
    y_dano, x_dano = [15, 60]
    y_vel_tiro, x_vel_tiro = [25,60]
    y_foguete, x_foguete = [7, 10]
    y_voltar, x_voltar = [altura_y - 5,60]

    #valores como parâmetro (soft coding)
    custo_upg_1 = 5
    custo_upg_2 = 10
    vida = status.vida
    dano = status.dano
    vel_tiro = status.lerdeza_tiro
    vel_tiro_lvl = [0, vel_tiro, 7, 1] #vel_tiro_lvl[1] indice é o lvl
    dano_lvl = [0, dano, 2, 3]
    vida_lvl = [0, vida, 4, 5]
    

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
        # se ENTER for apertado e a seta estiver em VIDA
        if codigo == 13 and y_seta == y_vida + 1:
            status.moedas, vida = melhorar_vida(status.moedas)
        # se ENTER or apertado e a seta estiver em DANO
        if codigo == 13 and y_seta == y_dano + 1:
            status.moedas, dano = melhorar_dano(status.moedas)
        # se ENTER or apertado e a seta estiver em VEL_TIRO
        if codigo == 13 and y_seta == y_vel_tiro + 1:
            status.moedas, vel_tiro = melhorar_vel_tiro(status.moedas)
        # se ENTER or apertado e a seta estiver em VOLTAR
        if codigo == 13 and y_seta == y_voltar:
            trocar_tela.trocar_tela("menu")
        #== MUDA A POSICAO DA SETA SEGUNDO INPUT ==
        y_seta = MudaCoordenadaYSetaIndicadora(codigo, y_seta, y_vida, y_voltar)
