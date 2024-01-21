# Métodos comuns
# Métodos de classe (Class methods)
# Métodos estáticos (Static methods)

class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram,
              self.placa_de_video, self.sistema_operacional)
        
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video - Baixo Custo')

    @classmethod
    def computador_configuracao_pesada(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video - Auto Custo')

    @staticmethod
    def roda_programs_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

computador1 = Computador.computador_escritorio('8gb')
computador2 = Computador.computador_configuracao_pesada('16gb')
computador1.exibir_dados_do_computador()
computador2.exibir_dados_do_computador()
print(Computador.roda_programs_pesados(10)) # Verifica se o computador roda programas pesados utilizando classe staticmethod
