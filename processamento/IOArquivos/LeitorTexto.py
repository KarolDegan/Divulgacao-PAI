from processamento.IOArquivos.InterfaceLeitorArquivo import InterfaceLeitorArquivo


class LeitorTexto(InterfaceLeitorArquivo):
    @staticmethod
    def ler(caminho: str):
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
