from enum import Enum
import re

class PadroesQuebra(Enum):

    NOME_PROJETO = re.compile(
         r'\s*(5\.\d+.?)?\s*([Nn]ome\s*do\s*projeto(?:/atividade)?:?)',
        re.IGNORECASE
    )

    DESCRICAO_PROJETO = re.compile(
        r'\s*([Dd]escri[çc][aã]o\s*(?:breve\s*)?do\s*projeto\s*(?:/atividade)?:?)',
        re.IGNORECASE
    )

    HIFEN = re.compile(
        r'(?<![A-Za-zÁ-ú])\s*[-–—]',
        re.IGNORECASE
    )

    NUMERACAO_POR_ALFABETO = re.compile(
        r'(?:^|[^a-zA-ZáàâãéèêíïóôõöúçÁÀÂÃÉÈÍÏÓÔÕÖÚÇ(])([a-záàâãéèêíïóôõöúç])\)'
    )

    NUMERACAO_POR_NUMERO = re.compile(
        r'\d\s*[\u2013\u2014]'
    )

    DOIS_PONTOS = re.compile(
        r'(?<!projeto/atividade):|(?<!x)\.:',
        re.IGNORECASE
    )

    BULLET = re.compile(
        r'\s*\u2022',
        re.IGNORECASE
    )

    NUMERO_ROMANO = re.compile(
        r'\s*[IVXL]+\s*[\u002D\u2013\u2014]\s*'
    )

    PONTO_VIRGULA = re.compile(
        r'\);|\b;',
        re.IGNORECASE
    )

    
    

    

