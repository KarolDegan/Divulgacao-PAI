from enum import Enum

class PadroesLixo(Enum):

    LIXO_RODAPE = (
        r'(APDO-TI\s*-\s*)?'                            
        r'(Plano de Atuação Institucional)'
        r'(\s*[A-Z]{3,10}\s*)?'             
        r'\s*(\()?'             
        r'\s*(\d{9})'
        r'(\)\s*)?'                                                               
        r'\s*(SEI)'                                     
        r'\s*(\d{4}\.\d{4}/\d{7}-\d\s*/\s*pg\.\s*\d+)'  
    )

    

    LIXO_TABELAS = (
        r'\s*(\()?'
        r'(Replicar\s*este\s*quadro\s*para\s*cada\s*projeto\s*ou\s*atividade\s*prevista\s*que\s*comp[õo]e\s*a\s*solicitaç[aã]o)'
        r'(\)\s*)?'
    )


    LIXO_FINAL_DOCUMENTO = (
        r'\s*(criado\s*por\s*)?'
        r'\s*(\s*[a-z]\d{6},?\s*)?'
        r'\s*(\s*vers[aã]o\s*\d)?'
        r'\s*(\s*\d\s*)?'
        r'\s*(\s*por\s*)?'
        r'\s*(\s*[a-z]\d{6},?\s*)?'
        r'\s*(\s*em\s*)?'
        r'\s*(?:\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}|\d{4}[/\-]\d{1,2}[/\-]\d{1,2})\s*'
        r'\s*(\d{2}:\d{2}:\d{2})?\s*'
    )

    