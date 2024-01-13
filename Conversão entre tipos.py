# Conversão entre tipos

idade = input('Digite a sua idade')
print(int(idade) > 17)

ano_publicação = 2020
print('Este livro foi criado em ' + str(ano_publicação))

#Conversões entre coleções

saudacao = 'Hello'
print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))
print(list(range(50)))

numeros = [10,20,20,50]
print(set(numeros))
print(tuple(numeros))
print(type(numeros))
