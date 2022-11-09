#importe da biblioteca de rotinas do jogo
from bibli import Jogador,Oponente,limpa_tela,delay_print

##################################################################################################################
#variaveis necessárias ao jogo
dano = 0.0

#Construção do personagem e do primeiro inimigo a ser enfrentado.

# criação de atributos do personagem
print('Bem vindo ao game doido do Humberto! \n Este jogo é um RPG de turnos onde a dificuldade avança junto com o seu nível.')
nome_personagem = input('Digite um nome para o seu personagem: ')
player = Jogador(nome_personagem)
player.subida_nivel()

#criação dos atributos do personagem inimigo 
inimigo = Oponente()
inimigo.born_inimigo(player.nivel)

###############################################################################################################################################################
#inicalização do jogo
#condições de saída do game:
#derrota vida == 0
#vitória nível == 100
while True:

    #chamada para subida de nível
    if player.xp == 100:
        print('Você subiu de nível!')
        player.subida_nivel()
        delay_print()
       # limpa_tela()

    #segunda condição de saída
    elif player.nivel == 100:
        print('Você venceu o jogo!')
        break

    elif player.vida <= 0.0:
        print('Você morreu!')
        break
 
    #modo de combate
    while True:

        if player.vida > 0 and player.nivel < 100 and player.xp < 100:

            dano = player.causar_dano()
            print(f'{player.nome} causou um dano de:\n{dano} \ne roubou:')
            inimigo.receber_dano(dano)
            print(f'Vida de {player.nome} = {player.vida}\nVida do inimigo = {inimigo.vida}')
            print('\n')
            delay_print()

            if inimigo.vida > 0:
                
                dano_enemy = 0.0
                dano_enemy = inimigo.causar_dano()
                print(f'O inimigo causou um dano de: {dano_enemy}\ne roubou:')
                player.receber_dano(dano_enemy)
                print(f'Vida de {player.nome} = {player.vida}\nVida do inimigo = {inimigo.vida}')
                print('\n')
                delay_print()

            else:
                player.xp += 1
                print('Você venceu esta batalha! Vamos ao próximo desafiante!')
                inimigo.born_inimigo(player.nivel)
                delay_print()
                limpa_tela()

        #condição de saída em caso de morte e saída do while de combate
        elif player.vida == 0:
            print('Você morreu!')
            break

        else:
            break











