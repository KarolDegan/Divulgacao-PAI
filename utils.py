import re

def padroes_nome_logico(nome_arquivo: str, tipo: int):
    padrao = re.match(r"^([A-Za-z0-9]+)(_)(\d+)(?:\.pdf)?(?:\.json)?$", nome_arquivo)
    
    if not padrao:
        print("Nome de arquivo inválido:", nome_arquivo)
        return None

    match tipo:
        case 1:
            return padrao.group(1) + padrao.group(2) + padrao.group(3)
        case 2:
            return padrao.group(1) + padrao.group(3)
        case 3:
            return padrao.group(1)
        case _:
            print("Tipo inválido:", tipo)
            return None
