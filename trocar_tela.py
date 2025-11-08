import jogo
import menu_melhorias
import menu

#trocar_tela vai ser o arquivo com todos os imports
#para ir para o jogo ou um menu, rodar trocar_tela("jogo")
def trocar_tela(caminho):
    match caminho:
        case "jogo": 
            jogo.jogo()
        case "menu_melhorias": 
            menu_melhorias.menu_melhorias()
        case "menu": 
            menu.menu()
        case _:
            print("nome do arquivo errado, trocar_tela(erro aqui!)")
