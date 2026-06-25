from enum import Enum

class PadroesTitulo(Enum):


    ORGAO = r'[ÓO]rg[aã]o\s*:?' # 0
    UNIDADE = r'[Uu]nidade\s*de\s*atu[aáãâà][cç][aáãâà]o\s*:?' # 1
    NOME_TITULAR = r'[Nn]ome\s*d[oa]\s*titular\s*d[oa]\s*[óo]rg[aáãâà]o(?:\s*ou\s*d[oa]\s*chefia\s*de\s*gabinete)?:?' # 2
    REGISTRO_FUNCIONAL = r'[Rr]egistro\s*funcional\s*d[oa]\s*titular\s*d[oa]\s*[óo]rgão(?:\s*ou?\s*d[oa]?\s*chefia\s*de\s*gabinete)?:?' # 3
    EMAIL_TITULAR = r'[Ee]-mail\s+d[oa]\s+titular(?:\s*d[oa]\s*[óo]rgão:?)(?:\s*ou?\s*d[oa]?\s*chefia\s*de\s*gabinete:?)?' # 4
    NOME_CHEFIA = r'[Nn]ome\s*da\s*chefia\s*imediata:?' # 5
    REGISTRO_CHEFIA = r'[Rr]egistro\s+funcional\s+da\s+chefia\s+imediata:?' # 6
    CARGO_CHEFIA = r'[Cc]argo\s+da\s+chefia\s+imediata:?' # 7
    EMAIL_CHEFIA = r'[Ee]-mail\s+da\s+chefia\s+imediata:?' # 8
    VIGENCIA_ALOCACAO = r'2\.\s+vigência\s+prevista\s+da\s+aloca[çc][aáãâà]o:?' # 9
    CONTEXTO_INTITUCIONAL = r'3\.\s+contexto\s+institucional(?:\s*/\s*desafios\s*a\s*serem\s*enfrentados\s*:?)?' # 10
    JUSTIFICATIVA = r'4\.\s*justificativa\s*da\s*solicita[cç][aã]o\s*:?' # 11
    ATIVIDADE_PREVISTA = r'5\.\s*Lista\s*de\s*projeto\(s\)\s*e/ou\s*atividade\(s\)(?:\s*previstas\s*para\s*o\s*APDO-TIC\s*:?\s*)?:?' # 12
    PERFIL_PROFICIONAL = r'6\.\s*Perfil\(is\)\s*profissional\(is\)\s*necessário\(s\)\s*:?' # 13
    FUNCOES_DESEMPENHADAS = r'7\.\s*Fun[cç][oõ]es\s*a\s*serem\s*desempenhadas\s*:?' # 14
    DECLARO_CIENTE = r'\s*(?:8\.s*)?\s*Declaro\s*estar\s*ciente\s*das\s*Leis,\s*:?' # 15
