import status

valores_status = [status.vida,status.dano,status.moedas,status.lerdeza_tiro,status.fase,status.onda]
def salvar():
    with open("save.txt", "w") as arquivo:
        for item in status.getValores():
            arquivo.write(str(item) + " ")
        print("Jogo salvo!")

def carregar():
    carregados = []

    with open("save.txt", "r") as arquivo:
        conteudo = arquivo.read().strip()
        if conteudo != '':
            for item in conteudo.split(" "):
                if item != '':
                    carregados.append(int(item))
        else:
            print("O save está vazio, criando um novo jogo...")
            novo_jogo()
            esperar(10000000)
            return
        
    status.vida = carregados[0]
    status.dano = carregados[1]
    status.moedas = carregados[2]
    status.lerdeza_tiro = carregados[3]
    status.fase = carregados[4]
    status.onda = carregados[5]
    print("carregando save...")
    esperar(10000000)

def novo_jogo():
    status.vida = 3
    status.dano = 1
    status.moedas = 0
    status.lerdeza_tiro = 13
    status.fase = 1
    status.onda = 0
    arquivo = open("save.txt", "w")
    arquivo.write("3 1 0 13 1 0")
    arquivo.close()
    print("Criando novo save...")
    esperar(10000000)

def esperar(segundos):
    cont = 0
    while cont < segundos:
        cont += 1