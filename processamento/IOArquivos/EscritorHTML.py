import os

class EscritorHTML:
    @staticmethod
    def escrever(conteudo: str, nome_para_arquivo: str):
        pasta_destino = "html"
        os.makedirs(pasta_destino, exist_ok=True)
        caminho = os.path.join(pasta_destino, f"{nome_para_arquivo}.html")

        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)