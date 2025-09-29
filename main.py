largura = 20
altura = 10

avião_x = largura // 2
tiro_y = -1
tiro_x = -1

# Cada inimigo é uma tupla (x, y)
inimigos = [(5, 0), (10, 0), (15, 0)]
acertos = 0


#Preenche a tela com caracteres 
while True:
    # Criar a tela vazia
    tela = []
    for y in range(altura):
        linha = ""
        for x in range(largura):
            if (x, y) in inimigos:
                linha += "@"
            elif y == tiro_y and x == tiro_x:
                linha += "|"
            elif y == altura - 1 and x == avião_x:
                linha += "^"
            else:
                linha += " "
        tela.append(linha)

    # Mostrar a tela
    for linha in tela:
        print(linha)

    print(f"Acertos: {acertos}/50")

    # Verifica colisão do tiro com inimigos
    if (tiro_x, tiro_y) in inimigos:
        inimigos.remove((tiro_x, tiro_y))
        acertos += 1
        tiro_y = -1
        print("Acertou!")

    # Verifica se atingiu 50 acertos
    if acertos >= 50:
        print("Você venceu com 50 acertos!")
        break

    # Verifica se algum inimigo alcançou o avião
    if any(y == altura - 1 for (x, y) in inimigos):
        print("Você foi atingido! Game Over.")
        break

    # Entrada do jogador
    comando = input("a=esq d=dir f=fogo: ")

    if comando == "a" and avião_x > 0:
        avião_x -= 1
    elif comando == "d" and avião_x < largura - 1:
        avião_x += 1
    elif comando == "f" and tiro_y == -1:
        tiro_x = avião_x
        tiro_y = altura - 2

    # Mover tiro
    if tiro_y >= 0:
        tiro_y -= 1

    # Mover inimigos para baixo
    inimigos = [(x, y + 1) for (x, y) in inimigos if y + 1 < altura]

    # Adiciona novos inimigos de tempos em tempos (opcional)
    if acertos % 5 == 0 and acertos != 0:
        inimigos.append((3, 0))
        inimigos.append((17, 0))

    print("\n" * 30)  # "Limpa" a tela
