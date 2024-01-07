#Cadastro usuario na empresa, onde utilizand random, fará um sorteio para verificar se aquele usuario ganhou um vale presente.
#Utilizando datetime para cadastrar a data e hora atual do cadastro e fazer conversões

from datetime import datetime
import random

print('*********OLA BEM VINDO A NOSSA EMPRESA!!!!******')
nome_usuario = input('Digita seu nome')
idade_usuario = input('Digite sua idade')
data_aniversario= datetime.strptime(input('Informe a data de seu aniversario no formato dd/mm/aaaa'), '%d/%m/%Y')
data_registro = datetime.now()

cartao = [50, 250, 120]
sorteiro1 = random.choice(cartao)
print(f'Parabens, você recebeu um cartão de R${sorteiro1}!')

print(f'Ola {nome_usuario} seu registro foi concluído com sucesso no dia {data_registro.day}/{data_registro.month}/{data_registro.year}')
