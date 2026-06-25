from controllers.ControllerProcessamentoPDF import *
from utils import padroes_nome_logico

import os

def gerar_instancias_pdf(pasta='./pdf/'):
    instancias = []
    for nome_arquivo in os.listdir(pasta):
        nome_logico = padroes_nome_logico(nome_arquivo,1)
        instancia_controller = ControllerProcessamentoPDF(f"{pasta}{nome_arquivo}")
        instancias.append((instancia_controller, nome_logico))
    return instancias
        



