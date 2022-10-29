#importação de bibliotecas auxiliares

#importe da biblioteca de rotinas do jogo
from bibli import *

##################################################################################################################

#declaração de variáveis a serem usadas no código

# criação de atributos do personagem
nome_personagem = ''
vitalidade = 0
forca = 0
furto = 0
vida = 100.0
nivel = 1
xp = 0

#criação dos atributos do personagem inimigo 
vitalidade_inimigo = 0
forca_inimigo = 0
furto_inimigo = 0
vida_inimigo = 0.0


#ciração de atributos auxiliares a subida de lv e inimigos
vida_temp_main = 0.0
vita_temp_main = 0
for_temp_main = 0
furto_temp_main = 0
xp_temp = 0

###############################################################################################################################################################

#inicalização do jogo
'''
#criação do personagem e instruções básicas
print('Bem vindo ao game doido do Humberto! \n Este jogo é um RPG de turnos onde a dificuldade avança junto com o seu nível.')
print('Para começar, vamos preencher os dados do seu personagem.\n')

#Inicialização do personagem com o preenchimento dos atributos de
while True:

    nome_personagem = input('Digite o nome do seu personagem: ')

    #recebimendo dos atributos no primeiro lV
    vita_temp_main,for_temp_main,vida_temp_main,furto_temp_main = subida_nivel(vitalidade,forca,vida,furto)

    print('\n Seu personagem está assim:')
    print('Seu nome será: ',nome_personagem)
    print(vita_temp_main,' Em vitalidade;')
    print(for_temp_main,' Em força;')
    print(furto_temp_main,' Em furto de vida;')
    print('nível: ',nivel)

    #validação para condição de saída
    validador_criacao_personagem = input('\n Digite R para refazer o personagem ou S para sair: ')

    if validador_criacao_personagem in 'Ss':

        #adição dos pontos atribuidos aos atributos principais
        vitalidade += vita_temp_main
        forca += for_temp_main
        vida = 0
        vida += vida_temp_main
        furto += furto_temp_main

        #zerando xp para reiniciar o avanço nas batalhas 
        xp = 0

         #limpeza de tela
        limpa_tela()

        #parada do while
        break

    #limpeza de tela em caso de repetição do while
    limpa_tela()

'''
#execução do game

#condições de saída do game:
#derrota vida == 0
#vitória nível == 100
while True:

    #ciração do adversário
    #zerando atribuitos para o novo combate
    vitalidade_inimigo = 0
    forca_inimigo = 0
    furto_inimigo = 0
    vida_inimigo = 0

    #chamada da função de criação do inimigo junto a atribuição dos valores de combate
    vitalidade_inimigo,forca_inimigo,furto_inimigo,vida_inimigo= born_inimigo(vitalidade_inimigo,forca_inimigo,furto_inimigo,vida_inimigo,nivel)
    
    #modo de combate
    







