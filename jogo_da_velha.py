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
    
    