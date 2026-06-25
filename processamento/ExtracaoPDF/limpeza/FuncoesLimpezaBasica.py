import unicodedata
import re

"""
Conjunto de funções para limpeza e normalização básica de texto.
"""

class FuncoesLimpezaBasica:
    @staticmethod
    def normalizar_unicode(texto: str) -> str:
        return unicodedata.normalize('NFC', texto)

    @staticmethod
    def limpar_unicode_invisivel(texto: str) -> str:
        texto = re.sub(r'[\u200B-\u200D\uFEFF]', '', texto)
        texto = re.sub(r'\s+', ' ', texto)
        return texto

    @staticmethod
    def remover_quebras_tabs(texto: str) -> str:
        return texto.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    
    @staticmethod
    def limpar_sobra(string):
        string = re.sub(r'^[\s\S]*?(?=<br>)', '', string, count=2)

        return string

