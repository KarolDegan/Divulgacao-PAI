# Divulgação PAI

Sistema automatizado de extração, processamento e geração de páginas HTML a partir de arquivos PDF contendo informações sobre projetos e atividades (PAI - Programa de Ações Integradas). O projeto converte dados extraídos de PDFs em estruturas JSON organizadas e as transforma em páginas HTML formatadas e interativas.

---

## 📋 Visão Geral

Este projeto foi desenvolvido para simplificar a divulgação de informações sobre projetos e atividades através de um pipeline automatizado:

1. **Extração**: Lê arquivos PDF e extrai o conteúdo textual usando múltiplas estratégias
2. **Limpeza**: Remove caracteres inválidos, normaliza unicode e aplica padrões de limpeza
3. **Processamento**: Estrutura dados em dicionários organizados
4. **Serialização**: Converte dicionários em arquivos JSON
5. **Visualização**: Gera páginas HTML renderizáveis

---

## 🏗️ Estrutura do Projeto

```
Divulgacao-PAI/
├── main.py                          # Orquestrador principal do pipeline
├── pdf_list.py                      # Gerador de instâncias de PDFs
├── utils.py                         # Funções utilitárias e padrões de nomes
│
├── controllers/                     # Camada de controle
│   ├── ControllerProcessamentoPDF.py    # Orquestra extração, limpeza e processamento de PDFs
│   └── ControllerGeradorHTML.py         # Gera arquivos HTML a partir de JSONs
│
├── processamento/                   # Lógica de processamento
│   ├── GeradorDicionarios.py            # Gera dicionários a partir de instâncias PDF
│   ├── PadronizarNomePDF.py             # Padroniza nomes de arquivos PDF
│   │
│   ├── ExtracaoPDF/                     # Módulo de extração e limpeza de PDFs
│   │   ├── ConversorPDF.py              # Converte PDFs em strings (fitz e pdfplumber)
│   │   ├── FormatadorTexto.py           # Formata e delimita textos com tags HTML
│   │   ├── limpeza/
│   │   │   ├── FuncoesLimpezaBasica.py  # Funções de normalização e limpeza básica
│   │   │   └── LimpezaPadroesRegex.py   # Limpeza com padrões regex
│   │   ├── extracao/
│   │   │   ├── InterfaceExtratorBase.py # Interface para extractors
│   │   │   ├── pdf/
│   │   │   │   └── ExtratorData.py      # Extrai datas dos PDFs
│   │   │   └── txt/
│   │   │       └── ExtratorTxt.py       # Extrai texto usando padrões
│   │   ├── pipelines/
│   │   │   ├── PipelineLimpeza.py       # Pipeline de limpeza em etapas
│   │   │   └── PipelineExtracao.py      # Pipeline de extração em etapas
│   │   └── verificador/                 # Módulo de verificação (em desenvolvimento)
│   │
│   ├── ConstrucaoHTML/                  # Módulo de construção de HTML
│   │   └── ConstrutorHTML.py            # Constrói tabelas e documento HTML completo
│   │
│   └── IOArquivos/                      # Módulo de I/O de arquivos
│       ├── LeitorUniversal.py           # Leitor genérico (JSON/TXT)
│       ├── LeitorJSON.py                # Leitor de arquivos JSON
│       ├── LeitorTexto.py               # Leitor de arquivos de texto
│       ├── EscritorUniversal.py         # Escritor genérico (JSON/HTML)
│       ├── EscritorJSON.py              # Escritor de arquivos JSON
│       ├── EscritorHTML.py              # Escritor de arquivos HTML
│       └── InterfaceLeitorArquivo.py    # Interface para leitores
│
├── enums/                           # Enumerações e padrões
│   ├── CompiladoraPadroes.py            # Compila padrões regex das enums
│   ├── NomesChaves.py                   # Chaves de campos extraídos
│   ├── PadroesTitulo.py                 # Padrões para identificar títulos
│   ├── PadroesLixo.py                   # Padrões de caracteres indesejados
│   ├── PadroesQuebra.py                 # Padrões para quebras de linha
│   ├── PadroesNumeroDocumento.py        # Padrões para números de documentos
│   ├── PadraoData.py                    # Padrão para extração de datas
│   └── Tags.py                          # Tags HTML utilizadas
│
├── css/                             # Estilos
│   └── estilo.css                       # Folha de estilos para HTML gerado
│
├── pdf/                             # Diretório de entrada (PDFs) - ignorado no git
├── json/                            # Diretório de intermediário (JSONs) - ignorado no git
├── html/                            # Diretório de saída (HTMLs) - ignorado no git
│
└── .gitignore                       # Configuração de arquivos ignorados
```

---

## 🔄 Fluxo de Funcionamento

### Pipeline Principal (`main.py`)

```
1. Padronização de Nomes
   └─> PadronizarNomePDF.padronizar_nome_pdfs()
       Renomeia PDFs para formato: [SIGLA]_[NUMERO].pdf

2. Geração de Instâncias
   └─> gerar_instancias_pdf()
       Cria ControllerProcessamentoPDF para cada PDF

3. Geração de Dicionários
   └─> GeradorDicionarios.gerar_todos_dicionarios()
       Processa cada PDF e gera dicionário de dados

4. Serialização em JSON
   └─> EscritorUniversal.escritor()
       Escreve dicionários em arquivos JSON

5. Geração de HTML
   └─> ControllerGeradorHTML.gerar_html()
       Lê JSONs e gera páginas HTML
```

### Pipeline de Extração de PDF (`ControllerProcessamentoPDF.py`)

```
Entrada: arquivo.pdf
  │
  ├─> Conversão: PDF → String
  │   ├─ ConversorPDF.para_string_fitz()     (via PyMuPDF/fitz)
  │   └─ ConversorPDF.para_string_pdfplumber() (via pdfplumber)
  │
  ├─> Limpeza: String → String Limpo
  │   ├─ Normalizar Unicode
  │   ├─ Remover quebras e tabs
  │   ├─ Limpar Unicode invisível
  │   └─ Aplicar padrões regex
  │
  ├─> Delimitação: Identificar seções
  │   ├─ Delimitar por títulos
  │   ├─ Delimitar por números de documento
  │   └─ Inserir quebras de formatação
  │
  ├─> Extração: String → Dicionário
  │   ├─ ExtratorUltimaData(): Extrai últimas datas
  │   ├─ ExtratorTxt(): Extrai campos por padrão
  │   └─ Múltiplas rodadas com diferentes padrões
  │
  └─> Saída: {"campo1": "valor1", "campo2": "valor2", ...}
```

---

## 📚 Módulos Principais

### `controllers/`

#### `ControllerProcessamentoPDF`
- **Responsabilidade**: Orquestrar o processamento completo de um PDF
- **Métodos principais**: `processar_extracao_pdf()`
- **Retorno**: Dicionário com campos extraídos

#### `ControllerGeradorHTML`
- **Responsabilidade**: Gerar HTML a partir de JSON
- **Métodos principais**: `gerar_html(arquivo_json, nome_para_html)`
- **Retorno**: Arquivo HTML gerado e salvo

---

### `processamento/ExtracaoPDF/`

#### `ConversorPDF`
Converte PDFs em strings usando dois métodos complementares:
- **fitz (PyMuPDF)**: Melhor para textos estruturados
- **pdfplumber**: Melhor para tabelas e layouts complexos

#### `FormatadorTexto`
Manipula strings de texto:
- `delimitar_txt()`: Marca seções usando padrões
- `inserir_tag_em_padrao()`: Insere tags HTML em padrões encontrados

#### `limpeza/`
**FuncoesLimpezaBasica**:
- `normalizar_unicode()`: Converte para NFC
- `remover_quebras_tabs()`: Remove `\n`, `\r`, `\t`
- `limpar_unicode_invisivel()`: Remove caracteres de controle
- `limpar_sobra()`: Remove fragmentos de conteúdo

**LimpezaPadroesRegex**:
- Aplica expressões regulares para remover padrões indesejados

#### `extracao/`
**ExtratorUltimaData**: Extrai a última ocorrência de data em formato DD/MM/YYYY

**ExtratorTxt**: Busca por padrões regex e extrai conteúdo:
- Aplica a `fila_nomes_chave` para nomear campos
- Remove duplicatas em cada campo

#### `pipelines/`
**PipelineLimpeza**: Encadeia funções de limpeza na ordem especificada

**PipelineExtracao**: Executa sequência de extractors em ordem

---

### `processamento/ConstrucaoHTML/`

#### `ConstrutorHTML`
Constrói estrutura HTML:
- `criar_tabelas_por_chave()`: Gera seções com tabelas para cada chave
- `gerar_html_completo()`: Envolve conteúdo em documento HTML válido
- Insere links para sistema SEI quando campo é "N° do processo"
- Formata valores com quebras de linha e espaçamento

---

### `processamento/IOArquivos/`

#### `LeitorUniversal` / `EscritorUniversal`
Interfaces genéricas que detectam tipo de arquivo automaticamente:
- Suportam `.json` e `.txt`
- Delegam para leitores/escritores específicos

#### `LeitorJSON` / `EscritorJSON`
Manipulam dados JSON estruturados

#### `LeitorTexto` / `EscritorTexto`
Manipulam arquivos de texto plano

---

### `enums/`

#### `CompiladoraPadroes`
Compila todas as enums em listas de regex compiladas com flag `IGNORECASE`:
```python
PADROES_TITULO = [re.compile(p.value, flags=re.IGNORECASE) for p in PadroesTitulo]
```

#### `NomesChaves`
Define campos que serão extraídos dos PDFs

#### Padrões
- **PadroesTitulo**: Identificam títulos de seções
- **PadroesLixo**: Caracteres/padrões a remover
- **PadroesQuebra**: Onde inserir quebras de linha
- **PadroesNumeroDocumento**: Formato de números de documentos
- **PadraoData**: Formato de datas (DD/MM/YYYY)

#### `Tags`
Constantes com tags HTML: `<br>`, `<strong>`, `<em>`, etc.

---

## 👤 Autor

Desenvolvido por Karol Degan

---

## 📞 Suporte

Para dúvidas ou problemas, consulte a documentação dos módulos específicos ou abra uma issue.

