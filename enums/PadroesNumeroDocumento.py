from enum import Enum

class PadroesNumeroDocumento(Enum):

    PROCESSO = r'Referência\s*:?\s+Processo\s+n\s*[º°]\s*'
    SEI = r'SEI\s*N\s*[º°]\s*:?\s*'