import fitz
import pdfplumber
from processamento.ExtracaoPDF.ConversorPDF import ConversorPDF
from processamento.ExtracaoPDF.limpeza.FuncoesLimpezaBasica import FuncoesLimpezaBasica
from processamento.ExtracaoPDF.limpeza.LimpezaPadroesRegex import LimpezaPadroesRegex
from enums.CompiladoraPadroes import CompiladoraPadroes
from processamento.ExtracaoPDF.pipelines.PipelineLimpeza import *
from processamento.ExtracaoPDF.pipelines.PipelineExtracao import *
from processamento.ExtracaoPDF.FormatadorTexto import *
from processamento.ExtracaoPDF.extracao.pdf.ExtratorData import ExtratorUltimaData
from processamento.ExtracaoPDF.extracao.txt.ExtratorTxt import ExtratorTxt
from enums.PadroesQuebra import PadroesQuebra
from enums.Tags import Tags
from enums.NomesChaves import NomesChaves



class ControllerProcessamentoPDF:
    def __init__(self, caminho_pdf):
        self.caminho_pdf = caminho_pdf
        self.doc_aberto_fiz = fitz.open(self.caminho_pdf)
        self.doc_aberto_pdfplumber = pdfplumber.open(self.caminho_pdf)
        self.dicionario = {}
        self.fila_nomes_chave = [(p.value) for p in NomesChaves]

    
    def processar_extracao_pdf(self):
        
        conversor = ConversorPDF(self.caminho_pdf, self.doc_aberto_fiz,self.doc_aberto_pdfplumber)
        string_pdfplumber = conversor.para_string_pdfplumber()
        

        string_fitz = conversor.para_string_fitz()
        

        #Limpar

        pipelineLimpeza = PipelineLimpeza([
            FuncoesLimpezaBasica.normalizar_unicode,
            FuncoesLimpezaBasica.remover_quebras_tabs,
            FuncoesLimpezaBasica.limpar_unicode_invisivel,
            LimpezaPadroesRegex(CompiladoraPadroes.REGEX_PADRAO_LIXO).aplicar

        ])
        

        string_pdfplumber_limpo = pipelineLimpeza.limpar(string_pdfplumber)
        string_fitz_limpa = pipelineLimpeza.limpar(string_fitz)        
        
        #Delimitar

        string_fitz_limpa_delimitada = FormatadorTexto.delimitar_txt(string_fitz_limpa,CompiladoraPadroes.PADROES_TITULO)

        string_pdfplumber_limpo_delimitado = FormatadorTexto.delimitar_txt(string_pdfplumber_limpo,CompiladoraPadroes.PADROES_TITULO[9:])

        string_pdfplumber_limpo_numero_delimitada = FormatadorTexto.delimitar_txt(string_pdfplumber_limpo_delimitado,CompiladoraPadroes.PADROES_N_DOCUMENTO)

        #Adicionando Quebras
        # Lista de padrões e como aplicar cada um
        pipeline = [
            (PadroesQuebra.BULLET.value, Tags.BR.value),
            (PadroesQuebra.NOME_PROJETO.value, Tags.STRONG_ABRE.value, Tags.STRONG_FECHA.value),
            (PadroesQuebra.DESCRICAO_PROJETO.value, Tags.EM_ABRE.value, Tags.EM_FECHA.value),
            (PadroesQuebra.DOIS_PONTOS.value, '', Tags.BR.value),
            (PadroesQuebra.NUMERO_ROMANO.value, Tags.BR.value),
            (PadroesQuebra.PONTO_VIRGULA.value,'',Tags.BR.value),
            (PadroesQuebra.NUMERACAO_POR_NUMERO.value, Tags.BR.value),
            (PadroesQuebra.NUMERACAO_POR_ALFABETO.value, Tags.BR.value)
        ]
        
        resultados_fitz = string_fitz_limpa_delimitada
        resultados_pdfplembler = string_pdfplumber_limpo_delimitado

        for item in pipeline:
            padrao = item[0]
            args = item[1:]
            
            resultados_fitz = FormatadorTexto.inserir_tag_em_padrao(resultados_fitz, padrao, *args)
            resultados_pdfplembler = FormatadorTexto.inserir_tag_em_padrao(resultados_pdfplembler,padrao,*args)

        string_fitz_limpa_delimitada_quebras = resultados_fitz
        string_pdfplumber_limpo_delimitado_quebras = resultados_pdfplembler

        # Extraçao
        
        pipelineExtracao = PipelineExtracao([
            lambda: ExtratorUltimaData(self.doc_aberto_fiz,self.dicionario).extrair(self.fila_nomes_chave),
            lambda: ExtratorTxt(string_pdfplumber_limpo_numero_delimitada,self.dicionario).extrair(CompiladoraPadroes.PADROES_N_DOCUMENTO,self.fila_nomes_chave),
            lambda: ExtratorTxt(string_fitz_limpa_delimitada,self.dicionario).extrair(CompiladoraPadroes.PADROES_TITULO[:9],self.fila_nomes_chave),
            lambda: ExtratorTxt(string_pdfplumber_limpo_delimitado_quebras,self.dicionario).extrair(CompiladoraPadroes.PADROES_TITULO[9:12],self.fila_nomes_chave),
            lambda: ExtratorTxt(string_fitz_limpa_delimitada_quebras,self.dicionario).extrair(CompiladoraPadroes.PADROES_TITULO[12:13],self.fila_nomes_chave),
            lambda: ExtratorTxt(string_pdfplumber_limpo_delimitado_quebras,self.dicionario).extrair(CompiladoraPadroes.PADROES_TITULO[13:-1],self.fila_nomes_chave)
            
        ])
        
        pipelineExtracao.extrair()
        

        #sobra de texto do pgm5
        indice = 15  # 12º item
        chave_15 = list(self.dicionario.keys())[indice]
        

        # acessar ou modificar o valor dessa chave
        valor = self.dicionario[chave_15]
        self.dicionario[chave_15] = FuncoesLimpezaBasica.limpar_sobra(valor)
        
        return self.dicionario
        



        





