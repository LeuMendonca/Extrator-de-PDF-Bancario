import PyPDF2 
from core.settings import MEDIA_ROOT
import pandas as pd 

def gera_excel_itau(arquivo,nome_arquivo):
    arquivo_pdf = PyPDF2.PdfReader(arquivo)
    total_paginas =   len(arquivo_pdf.pages)

    lista_pagador = []
    lista_beneficiario = []
    lista_cnpj_beneficiario = []
    lista_data_pagamento = []
    lista_data_vencimento = []
    lista_valor_desconto = []
    lista_valor_multa = []
    lista_valor_documento = []
    lista_valor_pagamento = []
    lista_autenticacao = []
    
    for i in range(total_paginas):
        texto_extraido = arquivo_pdf.pages[i].extract_text().split("\n")
        
        pagador = ''
        beneficiario = ''
        cnpj_beneficiario = ''
        data_pagamento = ''
        data_vencimento = ''
        valor_desconto = '0,00'
        valor_multa = '0,00'
        valor_documento = '0,00'
        valor_pagamento = '0,00'
        autenticacao = ''


        for j in texto_extraido:
            if "Tributos Estaduais" in j or "Tributos Municipais" in j:
                for indice in arquivo_pdf.pages[i].extract_text().split("\n"):
                    if "Nome:" in indice:
                        pagador = indice.replace("Nome:","").strip()
                    if "Valor do documento" in indice:
                        valor_documento = indice.replace("Valor do documento:","").strip()
                        valor_pagamento = indice.replace("Valor do documento:","").strip()
                    
                    if "Operação efetuada em" in indice:
                        data_pagamento = indice.split()[3]
                    
                    if "Autenticação:" in indice:
                        autenticacao = texto_extraido[texto_extraido.index(indice) + 1]
                    beneficiario = 'Tributos Estaduais'
            
            if "(-) Desconto (R$):" in j:
                valor_desconto = texto_extraido[texto_extraido.index(j) + 1].strip()
                    
            if ' Valor do boleto (R$);' in j:
                valor_documento = texto_extraido[texto_extraido.index(j) + 1].strip()
                
            if "(+)Mora/Multa (R$):" in j:
                valor_multa = texto_extraido[texto_extraido.index(j) + 1].strip()
            
            if "Pagador:" in j:
                pagador = " ".join(texto_extraido[texto_extraido.index(j) + 1].strip().split(" ")[:((texto_extraido[texto_extraido.index(j) + 1].strip()).split(" ").index(""))])
                valor_pagamento = texto_extraido[texto_extraido.index(j) + 1].strip().split()[-1]
                
                
            if 'CPF/CNPJ do beneficiário:' in j:
                cnpj_beneficiario = texto_extraido[texto_extraido.index(j) + 1].strip().split()[-2]
                data_vencimento = texto_extraido[texto_extraido.index(j) + 1].strip().split()[-1]
                beneficiario = j.split(":")[1].replace("CPF/CNPJ do beneficiário","").strip()

            if ' Data de pagamento:' in j:
                data_pagamento = texto_extraido[texto_extraido.index(j) + 1].strip()
            
            if ' Beneficiário Final:  CPF/CNPJ do beneficiário final:  (=) Data de pagamento:' in j:
                data_pagamento = texto_extraido[texto_extraido.index(j) + 1].strip().split()[-1]


            
            if "Autenticação mecânica" in j:
                autenticacao = texto_extraido[texto_extraido.index(j) + 1].strip().split()[0]
        
        lista_pagador.append(pagador)
        lista_beneficiario.append(beneficiario)
        lista_cnpj_beneficiario.append(cnpj_beneficiario)
        lista_data_pagamento.append(data_pagamento)
        lista_data_vencimento.append(data_vencimento)
        lista_valor_desconto.append(valor_desconto)
        lista_valor_multa.append(valor_multa)
        lista_valor_documento.append(valor_documento)
        lista_valor_pagamento.append(valor_pagamento)
        lista_autenticacao.append(autenticacao)
            
    excel = {
        "Pagador" : lista_pagador,
        "Beneficiario" : lista_beneficiario,
        "CNPJ Beneficiario" : lista_cnpj_beneficiario,
        "Data de Pagamento" : lista_data_pagamento,
        "Data de Vencimento" : lista_data_vencimento,
        "Desconto" : lista_valor_desconto,
        "Multa" : lista_valor_multa,
        "Valor Documento" : lista_valor_documento,
        "Valor Pagamento" : lista_valor_pagamento,
        "Autenticação" : lista_autenticacao
    }

    arquivo_excel = pd.DataFrame(excel)
    arquivo_excel.to_excel(f"{MEDIA_ROOT}/{nome_arquivo}.xlsx",index=False)
