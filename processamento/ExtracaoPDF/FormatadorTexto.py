import re
from enums.CompiladoraPadroes import CompiladoraPadroes
from enums.Tags import Tags

class FormatadorTexto:

    """
 
    """

    @staticmethod
    def delimitar_txt(string_limpa, lista_de_padroes: CompiladoraPadroes):
        
        lista_padroes = lista_de_padroes

        linhas = string_limpa


        for padrao in lista_padroes:
            # função que adiciona '$%' delimitadores de texto 
            linhas = re.sub(
                padrao,
                lambda m: '$%' + m.group(0),  
                linhas,
                count =1,
            )


        return linhas
    
    @staticmethod
    def inserir_tag_em_padrao(string, padrao,tag_abertura:Tags = '', tag_fechamento:Tags = ''):
        
        linhas = string
                
        linhas = re.sub(
            padrao,
            lambda m: tag_abertura + m.group(0) + tag_fechamento,
            linhas
        )
        
        return linhas