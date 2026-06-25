import json
from processamento.IOArquivos.InterfaceLeitorArquivo import InterfaceLeitorArquivo

class LeitorJSON(InterfaceLeitorArquivo):
    @staticmethod
    def ler(caminho: str):
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)