import jogo
import menu_melhorias
import menu
import menu_fases

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
        case "menu_fases": 
            menu_fases.menu_fases()
        case _:
            print("nome do arquivo errado, trocar_tela(erro aqui!)")