import os
import re

class PadronizarNomePDF:
    @staticmethod
    def padronizar_nome_pdfs() -> dict:

        pasta = r"./pdf/"

        contagem = {}
        

        # Passo 1: escanear a pasta e identificar as numerações já existentes
        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.lower().endswith(".pdf"):
                
                match = re.match(r"^([A-Za-z0-9]+)_(\d+)\.pdf$", nome_arquivo)
                
                if match:
                    sigla = match.group(1).lower()
                    
                    numero = int(match.group(2))
                    
                    contagem[sigla] = max(contagem.get(sigla, 0), numero)
                    

        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.lower().endswith(".pdf") and "-" in nome_arquivo:
                
                sigla = nome_arquivo.split("-")[0].strip().lower()
                
                contagem[sigla] = contagem.get(sigla, 0) + 1
                novo_nome = f"{sigla}_{contagem[sigla]}.pdf"

                caminho_antigo = os.path.join(pasta, nome_arquivo)
                caminho_novo = os.path.join(pasta, novo_nome)

                if not os.path.exists(caminho_novo):
                    os.rename(caminho_antigo, caminho_novo)
                    
                    print(f"Renomeado: {nome_arquivo} → {novo_nome}")
                    continue
