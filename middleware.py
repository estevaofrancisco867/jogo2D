import jogo
import menu_melhorias
import menu

#middleware é um arquivo entre outros
#para ir para o jogo ou um menu, rodar middleware("jogo")
def middleware(caminho):
    if caminho == "jogo":
        jogo.jogo()
    elif caminho == "menu_melhorias":
        menu_melhorias.menu_melhorias()
    elif caminho == "menu":
        menu.menu()
    else: print("nome do arquivo errado, middleware(erro aqui!)")