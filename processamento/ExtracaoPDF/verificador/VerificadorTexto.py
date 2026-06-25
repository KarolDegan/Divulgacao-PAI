from enums.CompiladoraPadroes import CompiladoraPadroes

class VerificadorTexto:

    """
    Classe responsável por verificar se um conjunto de padrões regex está presente
    em uma página específica de um arquivo PDF.
    """
    
    @staticmethod
    def encontrou_padroes_na_pagina(doc_aberto_fitz, numero_pagina: int, padroes: CompiladoraPadroes) -> bool:
        pagina = doc_aberto_fitz[numero_pagina]
        blocos = pagina.get_text("blocks")

        for bloco in blocos:
            texto = bloco[4].replace("\n", " ").strip()
            for padrao in padroes:
                if padrao.search(texto):
                    return True
        return False