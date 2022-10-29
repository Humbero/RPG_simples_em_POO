#IMPORT DA BIBLIOTECA TIME PARA ADICIONAR DALAY ENTRE OS EVENTO DO GAME
#OBS: ESTE ITEM NÃO FOI DADO EM SALA
from time import sleep
import random

###################################################################
#criação da super classe jogador
class Personagem():

    #método constutor da classe
    def __init__(self):
        self.vitalidade = 0.0
        self.forca = 0.0
        self.furto = 0.0
        self.vida = 100
        self.nivel = 1

    #função de cálculo do dano e roubo de vida
    def dano_causado (forca,roubo):##################precisa de ajuste############

        #criação de temporárias
        temp_for = forca
        temp_roubo = roubo

        #calculo do dano causado + dano do roubo de vida
        dano = float((10 * forca)*(temp_roubo/1000))

        #calculo da vida roubada durante o dano causado
        vida_roubada = float(dano / (temp_roubo/100))

        return (dano,vida_roubada)
        
#classe jogador
class Jogador(Personagem):

    #metodo construtor com herança
    def __init__(self,nome,xp=0):
        self.nome = nome
        self.xp = xp
        super().__init__()

        '''função para adicionar os pontos ao subir de nível do usuário, lembrando que são apenas 03 pontos que
    o usuário ganha por nível e deve distribuir estes como desejar entre os atributos disponíveis'''
    def subida_nivel ():############ precisa de ajuste#############

        vita_temp = 0
        for_temp = 0
        furto_temp = 0
        

        print(' Você possui o seguinte status: \n Vitalidade:' '\n Força:',forca,'\n Furto de vida:',furto,'\n')
        
        #while para validar a distribuição antes de retornar
        while True:

            #zerando os valores para evitar bug na subida de lv
            vita_temp = 0
            for_temp = 0
            furto_temp = 0

            #for para disponibilizar os atributos a distribuição
            for n in range (3):

                x = n
                print('Vamos distribuir seus pontos? Você possui ', 3 - x,' Pontos para distribuir')
                teste_distribuicao = input('Digite V, F ou L(V: vitalidade,F:força,L:roubo de vida): ')

                #teste de adição dos pontos 
                if teste_distribuicao in 'Vv':
                    vita_temp += 1

                elif teste_distribuicao in 'Ff':
                    for_temp += 1

                elif teste_distribuicao in 'Ll':
                    furto_temp += 1

            #apresentação da distribuição feita 
            print('\n Você irá adicionar os seguites pontos:')
            print(vita_temp,' Em vitalidade;')
            print(for_temp,' Em força;')
            print(furto_temp,' Em furto de vida;')

            #solicitação de confirmação
            validador_distribuicao = input('Digite S para sim e N para não: ')

            #caso positivo adição dos valores e saída
            if validador_distribuicao in 'Ss':
                vitalidade += vita_temp
                forca += for_temp
                furto += furto_temp
                break
            

        #calculo de vida total do personagem
        vida = float( 100 + (10 * vitalidade))
       
#classe oponente
class Oponente(Personagem):

    #metodo construtor com herança
    def __init__(self):
        super().__init__()

    #função para criação dos atributos do inimigo
    #OBS: ESTE ITEM "random" NÃO FOI DADO EM SALA
    #####################precisa de ajuste###########################
    def born_inimigo (vita_ene,for_ene,furto_ene,vida_ene,lv_player):
        
        #declaração de variaveis temporárias
        vita_temp = 0
        for_temp = 0
        furto_temp = 0
        vida_temp = 50


        #calculando os pontos a serem distribuidos 
        pontos_inimigo = (3 * lv_player)

        #distribuição dos pontos 
        while pontos_inimigo > 0:

            #gerador de seleção dos atributos
            atribuidor = random.randint (1,3)

            #para atribuição a vida
            if atribuidor == 1:

                #geração do valor a ser atribuido
                temp_local = random.randint(0,pontos_inimigo)

                #adição do valor ao atribuito
                vita_temp += temp_local

                #dedução dos pontos atribuidos ao total disponivel para distribuição
                pontos_inimigo -= temp_local

            #para atribuição a força
            elif atribuidor == 2:

                #geração do valor a ser atribuido
                temp_local = random.randint(0,pontos_inimigo)

                #adição do valor ao atribuito
                for_temp += temp_local

                #dedução dos pontos atribuidos ao total disponivel para distribuição
                pontos_inimigo -= temp_local

            #para atribuição a furto de vida
            elif atribuidor == 3:

                #geração do valor a ser atribuido
                temp_local = random.randint(0,pontos_inimigo)

                #adição do valor ao atribuito
                furto_temp += temp_local

                #dedução dos pontos atribuidos ao total disponivel para distribuição
                pontos_inimigo -= temp_local
        
        #calculo dos pontos de vida do inimigo
        vida_ene = float( vida_temp + (10 * vita_temp))

        #atribuição dos pontos 
        vita_ene = vita_temp
        for_ene = for_temp
        furto_ene = furto_temp

        return vida_ene,for_ene,furto_ene,vida_ene


########################################################################################
#outras funções de uso

# comando para limpar o terminal durante a execução do game
def limpa_tela ():

    print(130 * '\n')

#função para adição de delay durante as jogadas de cada personagem 
#OBS: ESTE ITEM "sleep" NÃO FOI DADO EM SALA
def delay_print ():

    delay = 1.5

    sleep(delay)



    



