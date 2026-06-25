from utils import padroes_nome_logico
class ConstrutorHTML():
    def __init__(self, objeto_json):
        self.objeto_json = objeto_json

    def criar_tabelas_por_chave(self):
        
        html = ""

        for chave_principal, objeto_interno in self.objeto_json.items():
            # Section principal
            html += f'<section class="section-tabela {chave_principal}">\n'

            # Label que funciona como cabeçalho
            html += f'  <div class="cabecalho-linha">\n'
            html += f'    <div class="cabecalho-campo" colspan="2">\n'
            print(chave_principal)
            html += f'      <span class="cabecalho-nome">{padroes_nome_logico(chave_principal,3).upper()}</span>\n'
            html += f'    </div>\n'
            html += f'  </div>\n'
            

            # Corpo do “accordion” (simula tbody)
            html += f'<div class="corpo-tabela">\n'

            for campo, valor in objeto_interno.items():
                valor_formatado = str(valor).replace("<br><br><strong>Nome do projeto/atividade", "<strong>Nome do projeto/atividade", count=1)
                valor_formatado = valor_formatado.replace("<br><br><strong> Nome do projeto/atividade", "<strong>Nome do projeto/atividade", count=1)
                valor_formatado = valor_formatado.replace("\n", "<br>").replace("  ", "&nbsp;")

                html += f'<div class="corpo-tabela-linha {"-".join(campo.split())}">\n'
                html += f'  <div class="corpo-tabela-primeiro-campo">{campo}</div>\n'

                if campo == "N° do processo":
                    html += f'  <div class="corpo-tabela-segundo-campo"><a href="https://processos.prefeitura.sp.gov.br/Forms/consultarProcessos.aspx" target="_blank" class="link-sei">{valor_formatado}</a></div>\n'
                else:
                    html += f'  <div class="corpo-tabela-segundo-campo">{valor_formatado}</div>\n'

                html += f'</div>\n'  # fecha linha

            html += f'</div>\n'  # fecha corpo-tabela
            html += f'</section>\n'

        return html
    

    def gerar_html_completo(self, conteudo_tabelas):
        
        return f"""<!DOCTYPE html>
                <html lang="pt-br">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="../css/estilo.css">
                    <title>Tabela Pai</title>
                </head>
                <body>
                {conteudo_tabelas}
                </body>
                </html>
                """


