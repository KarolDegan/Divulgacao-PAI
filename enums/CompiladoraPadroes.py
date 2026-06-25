from enums.PadroesTitulo import PadroesTitulo
from enums.PadraoData import PadraoData
from enums.PadroesLixo import PadroesLixo
from enums.PadroesNumeroDocumento import PadroesNumeroDocumento
import re

"""
Compila os valores das Enums em padrões regex, ignorando maiusculas e minusculas, e os organiza em listas
"""

class CompiladoraPadroes():

    PADROES_TITULO = [re.compile(p.value, flags=re.IGNORECASE) for p in PadroesTitulo]
    PADROES_N_DOCUMENTO = [re.compile(p.value, flags=re.IGNORECASE) for p in PadroesNumeroDocumento]
    PADRAO_DATA = re.compile(PadraoData.PADRAO_DATA.value, flags=re.IGNORECASE)
    REGEX_PADRAO_LIXO = [re.compile(p.value, flags=re.IGNORECASE) for p in PadroesLixo]
    