#​​Desafios 🥇
#DESAFIO 1
#Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.
#A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
#Porém ela deve seguir as seguintes regras:

#1 - O primeiro argumento deve ser posicional
#2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados

def gerar_objeto_personalizado(cor,*,altura, formato):
    print(cor, altura, formato)

gerar_objeto_personalizado('preto', altura=2.10, formato='quadrado')

#DESAFIO 2 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
#DESAFIO 3 - Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, 
#porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.

def gerar_nome_completo(nome, sobrenome):
    print(f'Bem vindo {nome} {sobrenome}')

gerar_nome_completo('Gabriel', 'Dantas')

def calcular_valores(preco, quantidade=1):
    print(preco * quantidade)

calcular_valores(10, 2)
