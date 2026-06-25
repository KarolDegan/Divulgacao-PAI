import re

class LimpezaPadroesRegex():

    """
    Regra de limpeza que remove padrões específicos definidos por expressões regulares.

    Essa classe é útil para remoção de números, símbolos, links, ou qualquer padrão
    que possa ser definido por regex.
    """

    def __init__(self, padroes):
        self.padroes = padroes

    def aplicar(self, texto: str) -> str:
        for padrao in self.padroes:
            texto = re.sub(padrao, '', texto)
        return texto.strip()