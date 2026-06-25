from pdf_list import gerar_instancias_pdf
from processamento.GeradorDicionarios import GeradorDicionarios
from processamento.IOArquivos.EscritorUniversal import EscritorUniversal
from processamento.PadronizarNomePDF import PadronizarNomePDF
from controllers.ControllerGeradorHTML import *
from utils import padroes_nome_logico
import os


# 1. Padroniza nomes dos PDFs
PadronizarNomePDF.padronizar_nome_pdfs()

# 2. Gera os dicionários
instancias = gerar_instancias_pdf()
gerador_dados = GeradorDicionarios(instancias)
dicionarios = gerador_dados.gerar_todos_dicionarios()

# 3. Gera os JSONs
for nome_logico, dados in dicionarios.items():
    EscritorUniversal.escritor({nome_logico: dados}, f'{nome_logico}')

# 4. Gera os HTMLs a partir dos JSONs
pasta = './json/'

for nome_arquivo in os.listdir(pasta):
    nome_logico = padroes_nome_logico(nome_arquivo,1)
    ControllerGeradorHTML.gerar_html(f"{pasta}{nome_arquivo}",nome_logico)

