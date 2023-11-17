import PyPDF2
import pandas
from core.settings import MEDIA_ROOT

def gera_excel_santander(arquivo,nome_arquivo):

    arquivo_pdf = PyPDF2.PdfReader(arquivo)
    total_paginas = len(arquivo_pdf.pages)


    lista_pagador = []
    lista_beneficiario = []
    lista_data_vencimento = []
    lista_data_pagamento = []
    lista_valor_nominal = []
    lista_encargos = []
    lista_valor_total = []
    lista_autenticacao = []
        

    for i in range(total_paginas):
        texto_extraido = arquivo_pdf.pages[i].extract_text().split("\n")
        
        pagador = texto_extraido[0].split(":")[0].replace("Agência","").strip()
        beneficiario = ''
        data_vencimento = ''
        data_pagamento = ''
        valor_nominal = ''
        encargos = ''
        valor_total = ''
        autenticacao = ''
        
        try:
            extrair_beneficiario = texto_extraido[texto_extraido.index("Dados do Beneﬁciário Original"):texto_extraido.index('Dados do Pagador Original Dados do Pagador Efetivo')]
            for per in extrair_beneficiario:
                if "Nome Fantasia:" in per:
                    beneficiario = " ".join(extrair_beneficiario[:extrair_beneficiario.index(per)][1:]).split(":")[-1].strip()
        except:
            extrair_beneficiario = texto_extraido[texto_extraido.index("Dados do Beneﬁciário Original Dados do Sacador Avalista"):texto_extraido.index('Dados do Pagador Original Dados do Pagador Efetivo')]
            indice_inicial = 0
            indice_final = 0
            for p in range(len(extrair_beneficiario)):
                if "Razão Social:" in extrair_beneficiario[p]:
                    indice_inicial = extrair_beneficiario.index(extrair_beneficiario[p])
                if "Nome Fantasia:" in extrair_beneficiario[p]:
                    indice_final = extrair_beneficiario.index(extrair_beneficiario[p])
                    break
            beneficiario = " ".join(extrair_beneficiario[indice_inicial:indice_final]).replace("Razão Social:","").strip()
                
        for indice in texto_extraido:

            if "Valor Nominal:" in indice:
                valor_nominal = indice.replace("Valor Nominal:","").strip()
            
            if "Data da Transação:" in indice:
                data_pagamento = indice.replace("Data da Transação:","").strip()
            
            if "Valor Total a Cobrar:" in indice:
                valor_total = indice.replace("Valor Total a Cobrar:","").strip()
            
            if "Encargos:" in indice:
                encargos = indice.replace("Encargos:","").strip()
                
            if "Data de Vencimento:" in indice:
                data_vencimento = indice.replace("Data de Vencimento:","").strip()
            
            if "Número de Autenticação da Instituição Financeira Favorecida:" in indice:
                autenticacao = indice.replace("Número de Autenticação da Instituição Financeira Favorecida:","").strip()
        
        lista_pagador.append(pagador)
        lista_beneficiario.append(beneficiario)
        lista_data_vencimento.append(data_vencimento)
        lista_data_pagamento.append(data_pagamento)
        lista_valor_nominal.append(valor_nominal)
        lista_encargos.append(encargos)
        lista_valor_total.append(valor_total)
        lista_autenticacao.append(autenticacao)
        
        excel = {
            "Pagador" : lista_pagador,
            "Beneficiario" : lista_beneficiario,
            "Data de Vencimento" : lista_data_vencimento,
            "Data de Pagamento" : lista_data_pagamento,
            "Valor Nominal" : lista_valor_nominal,
            "Encargos" : lista_encargos,
            "Valor Total" : lista_valor_total,
            "Autenticação" : lista_autenticacao
        }
        
        arquivo_excel = pandas.DataFrame(excel)
        arquivo_excel.to_excel(f"{MEDIA_ROOT}/{nome_arquivo}.xlsx",index=False)