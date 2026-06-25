from enum import Enum

class PadraoData(Enum):

    PADRAO_DATA = padrao_data = r'\s*(?:\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}|\d{4}[/\-]\d{1,2}[/\-]\d{1,2})\s*'