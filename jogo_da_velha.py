def iniciar_tabuleiro():
    tabuleiro = []
    for _ in range(3):
        linha = [' '] * 3
        tabuleiro.append(linha)
    return tabuleiro

def exibir_tabuleiro(tabuleiro):
    print('\n   0   1   2')
    for i in range(3):
        print(f'{i}  {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]}')
        if i < 2:
            print('  -----------')
    print()

def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
    
    # Verificar colunas
    for j in range(3):
        if all(tabuleiro[i][j] == jogador for i in range(3)):
            return True
    
    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    
    return False

def verificar_empate(tabuleiro):
    
    for linha in tabuleiro:
        for celula in linha:
            if celula == ' ':
                return False
    return True

def jogar_velha():
    
    tabuleiro = iniciar_tabuleiro()
    jogador_atual = 'X'
    jogo_ativo = True
    
    print('Bem-vindo ao JOGO DA VELHA!')
    
    while jogo_ativo:
        exibir_tabuleiro(tabuleiro)
        print(f'É a vez do jogador: {jogador_atual}')
        
        valido = False
        while not valido:
            try:
                entrada_linha = input(f'Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): ')
                entrada_coluna = input(f'Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): ')
                
                linha = int(entrada_linha)
                coluna = int(entrada_coluna)
                
                if 0 <= linha <= 2 and 0 <= coluna <= 2:
                    if tabuleiro[linha][coluna] == ' ':
                        tabuleiro[linha][coluna] = jogador_atual
                        valido = True
                    else:
                        print('Essa célula já está ocupada. Tente novamente.')
                else:
                    print('Entrada inválida. Linha e coluna devem ser 0, 1 ou 2.')
                
            except ValueError:
                print('Entrada inválida. Por favor, insira números para linha e coluna.')
            except Exception as e:
                print(f'Ocorreu um erro: {e}. Tente novamente.')
        
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f'Parabéns! Jogador {jogador_atual} venceu!')
            jogo_ativo = False
        elif verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print('O jogo terminou em empate!')
            jogo_ativo = False
        else:
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    
    jogar_novamente = input('Deseja jogar novamente? (s/n): ').lower()
    if jogar_novamente == 's':
        jogar_velha()
    else:
        print('Obrigado por jogar!')

# Iniciar o jogo
if _name_ == "_main_":
    jogar_velha()