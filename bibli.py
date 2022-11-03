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
    def causar_dano(self):

        #calculo do dano causado + dano do roubo de vida
        dano = float((10 * self.forca)*(self.furto/1000))

        #calculo da vida roubada durante o dano causado
        #tratamento de erro em caso de furto de vida = 0
        try:
            vida_roubada = float(dano / (self.furto/100))
            print(f'roubo de {vida_roubada} de vida')
            self.vida += vida_roubada
            
            return (dano)
        except:
            print('Furto de vida = 0')

    #função para receber dano causado pelo adversário
    def receber_dano(self,dano):

        self.vida -= dano

        
#classe jogador
class Jogador(Personagem):

    #metodo construtor com herança
    def __init__(self,nome,xp=0):
        self.nome = nome
        self.xp = xp
        super().__init__()

    '''função para adicionar os pontos ao subir de nível do usuário, lembrando que são apenas 03 pontos que
    o usuário ganha por nível e deve distribuir estes como desejar entre os atributos disponíveis'''  
    def subida_nivel(self):

        #ariaveis temporárias de distribuição
        vita_temp = 0
        for_temp = 0
        furto_temp = 0
        
        #print do status atual do personagem para servir de parâmentro para a distribuição
        print(f' Você possui o seguinte status: \n Vitalidade:{self.vitalidade}\n Força:{self.forca}\n Furto de vida:{self.furto}\n')
        
        #while para validar a distribuição antes de retornar
        while True:

            #zerando os valores para evitar bug/acumulo na subida de lv
            vita_temp = 0
            for_temp = 0
            furto_temp = 0

            #for para disponibilizar os atributos a distribuição
            for n in range (3):
                
                #x = n para eviter conflito na distribuição e apresentar precisamente os atribuitos a serem distribuidos
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
                
                else:
                    print('Dado incorreto!')

            #apresentação da distribuição feita 
            print('\n Você irá adicionar os seguites pontos:')
            print(vita_temp,' Em vitalidade;')
            print(for_temp,' Em força;')
            print(furto_temp,' Em furto de vida;')

            #solicitação de confirmação
            validador_distribuicao = input('Digite S para sim e N para não: ')

            #caso positivo adição dos valores e saída
            if validador_distribuicao in 'Ss':
                self.vitalidade += vita_temp
                self.forca += for_temp
                self.furto += furto_temp
                break
            

        #calculo de vida total do personagem
        self.vida = float( 100 + (10 * self.vitalidade))
       
#classe oponente
class Oponente(Personagem):

    #metodo construtor com herança
    def __init__(self):
        super().__init__()

    #função para criação dos atributos do inimigo
    def born_inimigo (self,lv_player):

        #zerando dados do inimigo antes da sua criação
        self.forca = 0
        self.furto = 0
        self.vida = 50
        self.vitalidade = 0

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
                self.vitalidade += temp_local

                #dedução dos pontos atribuidos ao total disponivel para distribuição
                pontos_inimigo -= temp_local

            #para atribuição a força
            elif atribuidor == 2:

                #geração do valor a ser atribuido
                temp_local = random.randint(0,pontos_inimigo)

                #adição do valor ao atribuito
                self.forca += temp_local

                #dedução dos pontos atribuidos ao total disponivel para distribuição
                pontos_inimigo -= temp_local

            #para atribuição a furto de vida
            elif atribuidor == 3:

                #geração do valor a ser atribuido
                temp_local = random.randint(0,pontos_inimigo)

                #adição do valor ao atribuito
                self.furto += temp_local

                #dedução dos pontos atribuidos ao total disponivel para distribuição
                pontos_inimigo -= temp_local
        
        #calculo dos pontos de vida do inimigo
        self.vida = float( self.vida + (10 * self.vitalidade))


########################################################################################
#outras funções de uso

# comando para limpar o terminal durante a execução do game
def limpa_tela ():

    print(130 * '\n')

#função para adição de delay durante as jogadas de cada personagem 
#OBS: ESTE ITEM "sleep" NÃO FOI DADO EM SALA
def delay_print ():

    delay = 1.0

    sleep(delay)



    



