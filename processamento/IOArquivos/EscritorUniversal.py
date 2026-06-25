from processamento.IOArquivos.EscritorJSON import EscritorJSON
from processamento.IOArquivos.EscritorHTML import EscritorHTML

class EscritorUniversal:
    @staticmethod
    def escritor(conteudo, nome_para_arquivo: str):
        if isinstance(conteudo, dict):
            
            return EscritorJSON.escrever(conteudo, nome_para_arquivo)
        elif isinstance(conteudo, str):
            
            return EscritorHTML.escrever(conteudo, nome_para_arquivo)
        else:
            raise TypeError(
                f"Tipo de conteúdo não suportado: {type(conteudo).__name__}. "
                "Use dict para JSON ou str para HTML"
            )