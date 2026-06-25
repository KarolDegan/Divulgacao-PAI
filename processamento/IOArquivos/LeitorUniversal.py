from pathlib import Path
from processamento.IOArquivos import InterfaceLeitorArquivo
from processamento.IOArquivos.LeitorJSON import LeitorJSON
from processamento.IOArquivos.LeitorTexto import LeitorTexto

class LeitorUniversal: #Fabrica
    @staticmethod
    def leitor(caminho: str) -> InterfaceLeitorArquivo:
        extensao = Path(caminho).suffix.lower()
        if extensao == ".json":
            return LeitorJSON.ler(caminho)
        else:
            return LeitorTexto.ler(caminho)