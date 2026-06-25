"""
Essa é uma interface/abstração.
Todo tipo de “extracao” deve herdar dela e implementar aplicar.

"""

from abc import ABC, abstractmethod

class InterfaceExtratorBase(ABC):
    """
    Interface abstrata para extratores de dados.
    Todo extrator deve implementar o método extrair.
    """

    @abstractmethod
    def extrair(self, resultados: dict) -> None:
        pass
