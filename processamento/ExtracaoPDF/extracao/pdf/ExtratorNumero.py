from processamento.ExtracaoPDF.extracao.InterfaceExtratorBase import InterfaceExtratorBase
from enums.CompiladoraPadroes import CompiladoraPadroes
from processamento.ExtracaoPDF.verificador.VerificadorTexto import VerificadorTexto

class ExtratorNumero(InterfaceExtratorBase):

    """
    Extrai do PDF expecificaente o numero SEI e o numero do Processo, baseado em padrões definidos
    em CompiladoraPadroes.PADROES_N_DOCUMENTO.

    Não está sendo utilizada no momento
    """

    def __init__(self, doc_aberto_fitz, dicionario_resultados = {}):
        self.doc_aberto_fitz = doc_aberto_fitz
        self.dicionario_resultados = dicionario_resultados

    def extrair(self):


        
        indice = -1 if VerificadorTexto.encontrou_padroes_na_pagina(self.doc_aberto_fitz,-1,CompiladoraPadroes.PADROES_N_DOCUMENTO) else -2
    
        ultima_pagina = self.doc_aberto_fitz[indice]

        blocos = ultima_pagina.get_text("blocks")  

        for padrao in CompiladoraPadroes.PADROES_N_DOCUMENTO:
            for bloco in blocos:
                texto_bloco = bloco[4] 
                match = padrao.search(texto_bloco)
                if match:
                    depois_do_padrao = texto_bloco[match.end():].strip()
                    indice = match.group(0).strip()
                    
                    self.dicionario_resultados[indice] = depois_do_padrao
        
        
