# Montando Tabuleiro
print('Iniciando o jogo.')
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
for l in range(0, 3):
    for c in range(0, 3):
        print('[{}]'.format(matriz[l][c]), end='')
    print()

# Início do Jogo
j = 0
while j < 9:
    # Informar de quem é a vez.
    if (j % 2) == 0:
        print('Está na vez do Jogador X.')
    else:
        print('Está na vez do Jogador O.')

    # Receber jogada e atualizar a cédula.
    verificador = 0
    while verificador == 0:
        linha = int(input('Digite qual linha da sua jogada (entre 1 e 3). '))-1
        coluna = int(input('Digite qual a coluna da sua jogada (entre 1 e 3). '))-1
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print('Jogada fora do intervalo permitido, selecione outra posição.')
        elif matriz[linha][coluna] == 'X' or matriz[linha][coluna] == 'O':
            print('Jogada já realizada, selecione outra posição.')
        else:
            if (j % 2) == 0:
                matriz[linha][coluna] = 'X'
            else:
                matriz[linha][coluna] = 'O'
            verificador = 1

    # Apresentar condição atual do jogo.
    for l in range(0, 3):
        for c in range(0, 3):
            print('[{}]'.format(matriz[l][c]), end='')
        print()

    # Verificando se alguem ganhou.
    for L in range(0, 3):
        for C in range(0, 3):
            if C==0:
                if matriz[L][C] == matriz[L][C + 1] and matriz[L][C] == matriz[L][C + 2] and matriz[L][C] != ' ':
                    print('Fim de jogo. O Jogador {} ganhou!'.format(matriz[linha][coluna]))
                    j = 9
                    break
                elif L<1 and matriz[L][C] == matriz[L + 1][C] and matriz[L][C] == matriz[L + 2][C] and matriz[L][C] != ' ':
                    print('Fim de jogo. O Jogador {} ganhou!'.format(matriz[linha][coluna]))
                    j = 9
                    break
                elif L<1 and matriz[L][C] == matriz[L + 1][C + 1] and matriz[L][C] == matriz[L + 2][C + 2] and matriz[L][C] != ' ':
                    print('Fim de jogo. O Jogador {} ganhou!'.format(matriz[linha][coluna]))
                    j = 9
                    break
                elif L<1 and matriz[L][C] == matriz[L - 1][C + 2] and matriz[L][C] == matriz[L - 2][C + 2] and matriz[L][C] != ' ':
                    print('Fim de jogo. O Jogador {} ganhou!'.format(matriz[linha][coluna]))
                    j = 9
                    break
                elif L==2 and matriz[L][C] == matriz[L - 1][C + 1] and matriz[L][C] == matriz[L - 2][C + 2] and matriz[L][C] != ' ':
                    print('Fim de jogo. O Jogador {} ganhou!'.format(matriz[linha][coluna]))
                    j = 9
                    break
            else:
                if L<1 and matriz[L][C] == matriz[L+1][C] and matriz[L][C] == matriz[L+2][C] and matriz[L][C] != ' ':
                    print('Fim de jogo. O Jogador {} ganhou!'.format(matriz[linha][coluna]))
                    j = 9
                    break

    j = j + 1
    #print (j)
    if j==9:
        print('Fim de jogo. Ninguém ganhou.')


#C:\Users\mauri\PycharmProjects\pythonProject\venv\Scripts
#pip install auto-py-to-exe
#auto-py-to-exe
