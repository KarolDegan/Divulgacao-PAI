class VerificadorImagem:

    """
    Classe responsável por verificar se uma página específica de um arquivo PDF contém imagens.
    """
    
    @staticmethod
    def encontrou_imagem_na_pagina(doc_aberto_fitz, numero_pagina: int) -> bool:
        pagina = doc_aberto_fitz[numero_pagina]
        imagens = pagina.get_images(full=True)
        return bool(imagens)