#Desafio
#Com base nas listas de celulares e modelos, exiba na tela a marca do celular com seus respectivos modelos

celulares = ['Asus', 'Samsung', 'Sony', 'Iphone']
versoes = ['Plus','Premium Plus','Premium Deluxe', 'Plus Prmium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'{celular} {versao}')
