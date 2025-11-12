import status

valores_status = [status.vida,status.dano,status.moedas,status.lerdeza_tiro,status.fase,status.onda]
def salvar():
    with open("save.txt", "w") as arquivo:
        for item in status.getValores():
            arquivo.write(str(item) + " ")
        print("jogo salvo!")

def carregar():
    carregados = []

    with open("save.txt", "r") as arquivo:
        if len(arquivo.read()) > 0:
            for item in arquivo.read().split(" "):
                carregados.append(item)
            if len(carregados) > len(status.getValores()):
                carregados.pop()
            for i in range(len(carregados)):
                carregados[i] = int(carregados[i])
                valores_status[i] = carregados[i]
        else: print("Nenhum save encontrado. Inicie um novo jogo!")
    print(status.getValores())

def novo_jogo():
    status.vida = 3
    status.dano = 1
    status.moedas = 0
    status.lerdeza_tiro = 13
    status.fase = 1
    status.onda = 0
    arquivo = open("save.txt", "w")
    arquivo.write("")
    arquivo.close()
    print("Save deletado e status resetado!!")