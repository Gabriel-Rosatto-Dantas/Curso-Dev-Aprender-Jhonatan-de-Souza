from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, valor):
        pass
    @abstractmethod
    def diminuir_claridade(self, valor):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f'Aumentando a claridade do monitor para {valor}')
    def diminuir_claridade(self, valor):
        print(f'Diminuindo a claridade do monitor para {valor}')

monitor1 = MonitorFullHD()
monitor1.aumentar_claridade(5)
monitor1.diminuir_claridade(5)
