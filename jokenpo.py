counter = True

while counter is True:
    jogador1 = (input('Escolha uma das opções:  pedra, papel ou tesoura?'))
    jogador2 = (input('Escolha uma das opções:  pedra, papel ou tesoura?'))

    if jogador1 not in ['pedra', 'papel', 'tesoura'] or jogador2 not in ['pedra', 'papel', 'tesoura']:
     print('Digite uma informação válida')

    if (jogador1 == 'pedra') and (jogador2 == 'papel'):
     print('Papel ganhou')
     
    if (jogador1 == 'pedra') and (jogador2 == 'tesoura'):
     print('Pedra ganhou')
     
    if (jogador1 == 'papel') and (jogador2 == 'tesoura'):
     print('Tesoura ganhou')
     
    if (jogador1 == 'papel') and (jogador2 == 'pedra'):
     print('Papel ganhou')
     
    if (jogador1 == 'tesoura') and (jogador2 == 'pedra'):
     print('Pedra ganhou')
     
    if (jogador1 == 'tesoura') and (jogador2 == 'papel'):
     print('Tesoura ganhou')
     
    if (jogador1 == 'papel') and (jogador2 == 'papel'):
     print('Empate!')
     
    if (jogador1 == 'tesoura') and (jogador2 == 'tesoura'):
     print('Empate!')
     
    if (jogador1 == 'pedra') and (jogador2 == 'pedra'):
     print('Empate!')
     
