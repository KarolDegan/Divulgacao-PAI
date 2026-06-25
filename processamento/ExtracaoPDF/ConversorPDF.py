class ConversorPDF:

    """
    Converter PDF em string
    """

    def __init__(self, caminho_pdf, doc_aberto_fitz = None,doc_aberto_pdfplumber = None):
        self.caminho_pdf = caminho_pdf
        self.doc_fitz = doc_aberto_fitz
        self.doc_pdfplumber = doc_aberto_pdfplumber
    
    
    def para_string_pdfplumber(self) -> str:
        
        texto_final = ""

        for page in self.doc_pdfplumber.pages:
            texto_pagina = page.extract_text()
            
            if texto_pagina:  # evita None se a página estiver vazia
                texto_final += texto_pagina + "\n"

        return texto_final
    


    def para_string_fitz(self):

        texto_final = ""

        for pagina in self.doc_fitz:
            texto_pagina = pagina.get_text("text")
            
            if texto_pagina:
                texto_final += texto_pagina + "\n"

        return texto_final
