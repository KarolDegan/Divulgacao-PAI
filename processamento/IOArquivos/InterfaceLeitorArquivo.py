from abc import ABC, abstractmethod

class InterfaceLeitorArquivo(ABC):
    @abstractmethod
    def ler(self, caminho: str):
        pass
