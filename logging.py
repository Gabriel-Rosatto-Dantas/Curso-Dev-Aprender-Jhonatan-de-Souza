import logging

logging.basicConfig(Level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s') #Setar o nivel

try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha'))
    if senha =='1234':
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('Favor digitar apenas números')
    logging.warning(erro)
