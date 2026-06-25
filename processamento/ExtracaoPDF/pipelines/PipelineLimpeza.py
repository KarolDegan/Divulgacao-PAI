"""
serve para aplicar várias regras de limpeza de forma sequencial a um texto.
"""

class PipelineLimpeza:
    def __init__(self, funcoes_limpeza: list):
        self.funcoes_limpeza = funcoes_limpeza

    def limpar(self, texto: str) -> str:
        for func in self.funcoes_limpeza:
            texto = func(texto)
        return texto