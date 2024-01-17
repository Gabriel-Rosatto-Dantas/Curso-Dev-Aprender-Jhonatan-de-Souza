class Computador:
    def __init__(self, marca, memoria, placa_video):
        self.marca = marca
        self.memoria = memoria
        self.placa_video = placa_video
    
    def ligar(self):
        print('Estou ligando o computador')

    def desligar(self):
        print('Estou desligando')

    def exibir_informacoes_do_comptador(self):
        print(f'Computador da marca {self.marca}, com {self.memoria} de memória ram e que usa a placa de video {self.placa_video}')

computador1 = Computador('Asus', '8gb', 'NVIDIA')
computador1.ligar()
computador1.desligar()
computador1.exibir_informacoes_do_comptador()
