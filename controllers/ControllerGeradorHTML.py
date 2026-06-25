from processamento.ConstrucaoHTML.ConstrutorHTML import ConstrutorHTML
from processamento.IOArquivos.EscritorUniversal import EscritorUniversal
from processamento.IOArquivos.LeitorUniversal import LeitorUniversal

class ControllerGeradorHTML:
    @staticmethod
    def gerar_html(arquivo_json: str, nome_para_html: str):
        
        objeto_json = LeitorUniversal.leitor(arquivo_json)

        
        html = ConstrutorHTML(objeto_json)    #instancia construtor  
        conteudo_tabelas = html.criar_tabelas_por_chave()


        html_completo = html.gerar_html_completo(conteudo_tabelas)

        
        EscritorUniversal.escritor(html_completo,nome_para_html)

        print(f"Arquivo HTML gerado com sucesso")