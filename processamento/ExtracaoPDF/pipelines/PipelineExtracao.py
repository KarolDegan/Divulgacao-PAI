"""
serve para aplicar várias regras de extração de forma sequencial a um texto.
"""

class PipelineExtracao:
    def __init__(self, funcoes_extracao: list):
        self.funcoes_extracao = funcoes_extracao

    def extrair(self):
        for func in self.funcoes_extracao:
            func()

