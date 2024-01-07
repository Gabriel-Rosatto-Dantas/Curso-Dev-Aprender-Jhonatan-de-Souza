#Desafio 1
#Use a operação necessária(break ou continue) para que a seguinte condição aconteça.
#Ao chegar ao estilo "Rap" o mesmo não deve ser impresso na tela
#estilos = ['Hip-Hop','Rock','Rap','Pop']

#Desafio 2
#Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:

#Ao chegar ao estilo "Rock" a execução deve interrompida
#estilos = ['Hip-Hop','Rock','Rap','Pop']

estilos = ['Hip-Hop', 'Rock', 'Rap','Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)

estilos = ['Hip-Hop', 'Rock', 'Rap','Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)
