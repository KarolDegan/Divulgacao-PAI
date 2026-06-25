import json
import os

class EscritorJSON:
    @staticmethod
    def escrever(conteudo: dict, nome_para_arquivo: str):
        pasta_destino = "json"
        os.makedirs(pasta_destino, exist_ok=True)
        caminho = os.path.join(pasta_destino, f"{nome_para_arquivo}.json")

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(conteudo, f, ensure_ascii=False, indent=4)
