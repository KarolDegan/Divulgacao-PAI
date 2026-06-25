from processamento.ExtracaoPDF.extracao.InterfaceExtratorBase import InterfaceExtratorBase
from enums.CompiladoraPadroes import CompiladoraPadroes
from processamento.ExtracaoPDF.limpeza.FuncoesLimpezaBasica import FuncoesLimpezaBasica
import re

class ExtratorTxt(InterfaceExtratorBase):

    """
    Classe responsável por extrair informações de uma string delimitada usando padrões regex.

    Esta classe implementa a interface `InterfaceExtratorBase` e permite aplicar
    uma lista de padrões de forma sequencial, armazenando os resultados em um
    dicionário.
    """

    def __init__(self,string_delimitado, dicionario_resultados = {}):
        self.string_delimitado = string_delimitado
        self.dicionario_resultados = dicionario_resultados

    def extrair(self, extensao_padroes_titulo: CompiladoraPadroes, fila_nomes_chave):
        lista_padroes = extensao_padroes_titulo.copy() 

        texto = self.string_delimitado

        for padrao in lista_padroes:
            match = re.search(padrao, texto)
            if match:
                resto = texto[match.end():]
                conteudo = resto.split('$%')[0].strip()
                    
                indice = match.group(0)
                indice = FuncoesLimpezaBasica.limpar_unicode_invisivel(indice)
                indice = indice.strip()

                self.dicionario_resultados[fila_nomes_chave[0]] = conteudo

                fila_nomes_chave.pop(0)

        