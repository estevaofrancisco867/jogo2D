import jogo
import menu_melhorias
import menu
# def middleware():
#     jogo.jogo()
#     menu.menu()
#     menu_melhorias.menu_melhorias()

def middleware(caminho):
    if caminho == "jogo":
        jogo.jogo()
    elif caminho == "menu_melhorias":
        menu_melhorias.menu_melhorias()
    elif caminho == "menu":
        menu.menu()
    else: print("nome do arquivo errado, middleware(erro aqui)")