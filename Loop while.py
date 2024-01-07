#DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
#DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
#DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1

contador= 0
while contador <= 121:
    print(contador)
    contador += 1 

senha = ''
while senha != 'secreto':
    senha = input('Digite sua senha:')
print('Bem vindo') 

contador = 100
while contador >= 0:
    print(contador)
    contador - 1 
