# processamento/GeradorDicionarios.py
class GeradorDicionarios:
    def __init__(self, lista_instancias):
        self.lista_instancias = lista_instancias

    def gerar_todos_dicionarios(self):
        resultado = {}

        for instancia, nome_logico in self.lista_instancias:
            dados = instancia.processar_extracao_pdf()
            resultado[nome_logico] = dados
        
        return resultado

