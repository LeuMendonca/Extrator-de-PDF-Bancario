import PyPDF2
from core.settings import MEDIA_ROOT
import pandas as pd


def gera_excel_bradesco(arquivo,nome_arquivo):
    arquivo_pdf = PyPDF2.PdfReader(arquivo)
    total_paginas =  len(arquivo_pdf.pages)

        
    lista_pagador = []
    lista_beneficiario = []
    lista_cnpj_beneficiario = []
    lista_data_debito = []
    lista_data_vencimento = []
    lista_valor = []
    lista_desconto = []
    lista_abatimento = []
    lista_bonificacao = []
    lista_multa = []
    lista_juros = []
    lista_valor_total = []
    lista_autenticacao = []



    for i in range(total_paginas):
        texto_extraido = arquivo_pdf.pages[i].extract_text().split("\n")
        pagador = ''
        beneficiario = ''
        cnpj_beneficiario = ''
        data_debito = ''
        data_vencimento = ''
        valor = ''
        desconto = ''
        abatimento = ''
        bonificacao = ''
        multa = ''
        juros = ''
        valor_total = ''
        autenticacao = ''
        
        for j in texto_extraido:
            
            
            if "Beneficiário" in j:
                
                if "Nome Fantasia" in j:
                    texto_beneficiario = j.split(":")
                    
                    for bene in texto_beneficiario:
                        if "Nome Fantasia" in bene:
                            beneficiario=  bene.replace("Nome Fantasia","").strip()
                        
                        if "CPF/CNPJ Beneficiário" in bene:
                            cnpj_beneficiario = bene.replace("CPF/CNPJ Beneficiário","").strip()
                    lista_beneficiario.append(beneficiario)
                    lista_cnpj_beneficiario.append(cnpj_beneficiario)
                
                                
            if "Valor total" in j:
                texto_valor_total = j.split(":")
                for n in texto_valor_total:
                    
                    if "Nome do Pagador" in n:
                        pagador = n.replace("Nome do Pagador","").strip()
                    
                    if "Data de débito" in n:
                        data_debito = n.replace("Data de débito","").strip()
                    
                    if "Data de vencimento" in n:
                        data_vencimento = n.replace("Data de vencimento","").strip().split("Valor")[-1]
                                               
                        
                    if "Valor" in n and "Valor total" not in n:
                        valor = n[:n.index("Valor")]
                    
                    if "Desconto" in n:
                        desconto = n.replace("Desconto","").strip()
                        
                    if "Abatimento" in n:
                        abatimento = n.replace("Abatimento","").strip()
                    
                    if "Bonificação" in n:
                        bonificacao = n.replace("Bonificação","").strip()
                    
                    if "Multa" in n:
                        multa = n.replace("Multa","").strip()
                    
                    if "Juros" in n:
                        juros = n.replace("Juros","").strip()
                    
                    if "Valor total" in n:
                        valor_total = n.replace("Valor total","").strip()
                    
            if "Autenticação" in j:
                autenticacao = " ".join(texto_extraido[texto_extraido.index("Autenticação") + 1 :])
        
        lista_pagador.append(pagador)
        lista_data_debito.append(data_debito)
        lista_data_vencimento.append(data_vencimento)
        lista_valor.append(valor)
        lista_desconto.append(desconto)
        lista_abatimento.append(abatimento)
        lista_bonificacao.append(bonificacao)
        lista_multa.append(multa)
        lista_juros.append(juros)
        lista_valor_total.append(valor_total)
        lista_autenticacao.append(autenticacao)

    excel_bradesco = {
        'Pagador' : lista_pagador,
        'Beneficiario' : lista_beneficiario,
        "CNPJ Beneficiario" : lista_cnpj_beneficiario,
        'Data de Pagamento' : lista_data_debito,
        'Data de Vencimento' : lista_data_vencimento,
        'Valor' : lista_valor,
        'Desconto' : lista_desconto,
        'Abatimento' : lista_abatimento,
        'Bonificação' : lista_bonificacao,
        'Multa' : lista_multa,
        'Juros' : lista_juros,
        'Valor Total' : lista_valor_total,
        'Autenticação': lista_autenticacao
    }

    arquivo_excel = pd.DataFrame(excel_bradesco)
    arquivo_excel.to_excel(f"{MEDIA_ROOT}/{nome_arquivo}.xlsx",index=False)
