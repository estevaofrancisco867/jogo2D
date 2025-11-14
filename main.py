import WConio2  # pip install WConio2
import menu

# Caso o save.txt não exista, cria um ao executar o main.py
with open("save.txt", "a"):
    pass

menu.menu()