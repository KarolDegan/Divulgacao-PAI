from processamento.ExtracaoPDF.verificador.VerificadorImagem import VerificadorImagem
from enums.CompiladoraPadroes import CompiladoraPadroes
from processamento.ExtracaoPDF.extracao.InterfaceExtratorBase import InterfaceExtratorBase
import re

class ExtratorUltimaData(InterfaceExtratorBase):

    """
    Extrai a última data encontrada no documento PDF, usando os padrões definidos
    em CompiladoraPadroes.PADROES_DATA, e adiciona ao dicionário de resultados
    com a chave 'Data de referência'.
    """


    def __init__(self, doc_aberto_fitz, dicionario_resultados = {}):
        self.doc_aberto_fitz = doc_aberto_fitz
        self.dicionario_resultados = dicionario_resultados

    def extrair(self, fila_nomes_chave) -> dict:
        indice = -1 if VerificadorImagem.encontrou_imagem_na_pagina(self.doc_aberto_fitz, -1) else -2
        pagina = self.doc_aberto_fitz[indice]
        texto = pagina.get_text()
        
        datas_encontradas = re.findall(CompiladoraPadroes.PADRAO_DATA, texto)

        if datas_encontradas:
            
            self.dicionario_resultados[fila_nomes_chave[0]] = datas_encontradas[-1]
            fila_nomes_chave.pop(0)
            
        
