from PyPDF2 import PdfReader
from core.settings import MEDIA_ROOT
import pandas

def gera_excel_bb(arquivo,nome_arquivo):
    #arquivo_pdf = open(arquivo,"rb")

    pdf = PdfReader(arquivo)
    total_de_paginas = len(pdf.pages)

    lista_cliente = []
    lista_beneficiario = []
    lista_cnpj_beneficiario = []
    lista_data_pagamento = []
    lista_data_vencimento = []
    lista_juros = []
    lista_valor_pagamento = []
    lista_valor_total_pagamento = []
    lista_nosso_numero = []
    lista_numero_documento = []
    lista_autenticacao = []
    lista_tipo_documento = []


    for i in range(total_de_paginas):

        pagina = pdf.pages[i].extract_text()
        
        #Separação das linhas em lista
        lista_texto = pagina.split("\n")
    
        #Removendo espaços no começo e final 
        for dados in range(len(lista_texto)):
            lista_texto[dados] = lista_texto[dados].strip()
        ####################################
        for j in lista_texto:
            if j == "COMPROVANTE DE PAGAMENTO":
                
                cliente = ''
                beneficiario = ''
                cnpj_beneficiario = ''
                data_de_pagamento = ''
                data_de_vencimento = ''
                valor_juros = '0,00'
                valor_pagamento = ''
                valor_total = ''
                nosso_numero = ''
                numero_documento = ''
                autenticacao = ''
                tipo_documento = 'COMPROVANTE DE PAGAMENTO'
                
                for dados in lista_texto:
                    if "CLIENTE:" in dados:
                        cliente = dados.replace("CLIENTE:","").strip()

                    if "Convenio" in dados:
                        beneficiario = dados.replace("Convenio","").strip()
                    
                    if "CNPJ" in dados:
                        cnpj_beneficiario = dados.replace("CNPJ:","").strip()
                        
                    if "CNPJ/CEI/CPF" in dados:
                        cnpj_beneficiario = dados.replace("CNPJ/CEI/CPF","").strip()
                    
                    if "AG. ARRECADADOR" in dados :
                        beneficiario = lista_texto[lista_texto.index("AG. ARRECADADOR") + 1]
                    
                    if "Data do pagamento" in dados:
                        data_de_pagamento = dados.replace("Data do pagamento","").strip()
                    
                    
                    if "DATA DO PAGAMENTO" in dados:
                        data_de_pagamento = dados.replace("DATA DO PAGAMENTO","").strip()
                    
                    if "DATA DO VENCIMENTO" in dados:
                        data_de_vencimento = dados.replace("DATA DO VENCIMENTO","").strip()
                        
                    if "Valor Total" in dados:
                        valor_total = dados.replace("Valor Total","").strip()
                        valor_pagamento = dados.replace("Valor Total","").strip()
                        
                    if "VALOR DOS JUROS" in dados:
                        valor_juros = dados.replace("VALOR DOS JUROS","").strip()
                        
                    elif "VALOR TOTAL" in dados:
                        valor_total = dados.replace("VALOR TOTAL","").strip()
                        valor_pagamento = dados.replace("VALOR TOTAL","").strip()
                        
                    if "AUTENTICACAO" in dados:
                        autenticacao = dados
                    
                
                lista_cliente.append(cliente)
                lista_beneficiario.append(beneficiario)
                lista_cnpj_beneficiario.append(cnpj_beneficiario)
                lista_data_vencimento.append(data_de_vencimento)
                lista_data_pagamento.append(data_de_pagamento)
                lista_valor_pagamento.append(valor_pagamento)
                lista_juros.append(valor_juros)
                lista_valor_total_pagamento.append(valor_total)
                lista_nosso_numero.append(nosso_numero)
                lista_numero_documento.append(numero_documento)
                lista_autenticacao.append(autenticacao)
                lista_tipo_documento.append(tipo_documento)

                
            if j == "COMPROVANTE DE PAGAMENTO DE TITULOS":
                
                cliente = ''
                beneficiario = lista_texto[lista_texto.index("BENEFICIARIO:") + 1]
                cnpj_beneficiario = ''
                data_de_pagamento = ''
                data_de_vencimento = ''
                valor_pagamento = ''
                valor_juros = '0,00'
                valor_total = ''
                nosso_numero = ''
                numero_documento = ''
                autenticacao = ''
                tipo_documento = 'COMPROVANTE DE PAGAMENTO DE TITULOS'

                
                for dados in lista_texto:
                    if "CLIENTE:" in dados:
                        cliente = dados.replace("CLIENTE:","").strip()
                    
                    if "CNPJ" in dados:
                        cnpj_beneficiario = dados.replace("CNPJ:","").strip()
                        
                    if "NR. DOCUMENTO" in dados:
                        numero_documento = dados.replace("NR. DOCUMENTO","").strip()
                        
                    if "NOSSO NUMERO" in dados:
                        nosso_numero = dados.replace("NOSSO NUMERO","").strip()
                    
                    if "DATA DE VENCIMENTO" in dados:
                        data_vencimento = dados.replace("DATA DE VENCIMENTO","").strip()
                    
                    if "DATA DO PAGAMENTO" in dados:
                        data_de_pagamento = dados.replace("DATA DO PAGAMENTO","").strip()
                        
                    if "JUROS/MULTA" in dados:
                        valor_juros = dados.replace("JUROS/MULTA","").strip()
                        
                    if "VALOR DO DOCUMENTO" in dados:
                        valor_total = dados.replace("VALOR DO DOCUMENTO","").strip()

                    if "VALOR COBRADO" in dados:
                        valor_pagamento = dados.replace("VALOR COBRADO","").strip()    
                    
                    if "NR.AUTENTICACAO" in dados:
                        autenticacao = dados.replace("NR.AUTENTICACAO","").strip()
                
                lista_cliente.append(cliente)
                lista_beneficiario.append(beneficiario)
                lista_cnpj_beneficiario.append(cnpj_beneficiario)
                lista_data_pagamento.append(data_de_pagamento)
                lista_valor_pagamento.append(valor_pagamento)
                lista_juros.append(valor_juros)
                lista_valor_total_pagamento.append(valor_total)
                lista_nosso_numero.append(nosso_numero)
                lista_numero_documento.append(numero_documento)
                lista_autenticacao.append(autenticacao)
                lista_data_vencimento.append(data_vencimento)
                lista_tipo_documento.append(tipo_documento)

                        
            if j == "Comprovante Pix":
                
                cliente = ''
                beneficiario = ''
                documento = ''
                data_de_pagamento = ''
                data_de_vencimento = ''
                valor_pagamento = ''
                valor_juros = '0,00'
                valor_total = ''
                nosso_numero = ''
                numero_documento = ''
                autenticacao = ''
                tipo_documento = 'COMPROVANTE DE PIX'

                
                for dados in lista_texto:
                    
                    if "CLIENTE" in dados:
                        cliente = dados.replace("CLIENTE:","").strip()
                    
                    if "PAGO PARA:" in dados:
                        beneficiario = dados.replace("PAGO PARA:","").strip()
                    
                    if "CNPJ:" in dados:
                        documento = dados.replace("CNPJ:","").strip()
                    
                    if "CPF:" in dados:
                        documento = dados.replace("CPF:","").strip()
                        
                    if "VALOR:" in dados:
                        valor_pagamento = dados.replace("VALOR:","").strip()
                        valor_total = dados.replace("VALOR:","").strip()
                    
                    if "DATA:" in dados:
                        data_de_pagamento = dados.replace("DATA:","").strip()
                    
                    if "DOCUMENTO" in dados:
                        numero_documento = dados.replace("DOCUMENTO:","").strip()

                    if "AUTENTICACAO SISBB:" in dados:
                        autenticacao = dados.replace("AUTENTICACAO SISBB:","").strip()
            
                lista_cliente.append(cliente)
                lista_beneficiario.append(beneficiario)
                lista_cnpj_beneficiario.append(documento)
                lista_data_pagamento.append(data_de_pagamento)
                lista_data_vencimento.append(data_de_vencimento)
                lista_valor_pagamento.append(valor_pagamento)
                lista_juros.append(valor_juros)
                lista_valor_total_pagamento.append(valor_total)
                lista_nosso_numero.append(nosso_numero)
                lista_numero_documento.append(numero_documento)
                lista_autenticacao.append(autenticacao)
                lista_tipo_documento.append(tipo_documento)

            
            if j == "COMPROVANTE DE DEBITO AUTOMATICO":

                
                cliente = ''
                beneficiario = ''
                cnpj_beneficiario = ''
                data_de_pagamento = ''
                data_de_vencimento = ''
                valor_pagamento = ''
                valor_juros = '0,00'
                valor_total = ''
                nosso_numero = ''
                numero_documento = 'REM '
                autenticacao = ''
                tipo_documento = 'COMPROVANTE DE DEBITO AUTOMATICO'


                
                for dados in lista_texto:
                    if "CLIENTE" in dados:
                        cliente = dados.replace("CLIENTE:","").strip()
                    
                    if "CONVENIO" in dados:
                        beneficiario = " - ".join(dados.replace("CONVENIO:","").strip().split())
                    
                    if "DATA DO DEBITO:" in dados:
                        data_de_pagamento = dados.replace("DATA DO DEBITO:","").replace(".","/").strip()

                    if "VALOR DO DEBITO" in dados:
                        valor_pagamento = " ".join(dados.replace("VALOR DO DEBITO","").strip().split())
                        valor_total = " ".join(dados.replace("VALOR DO DEBITO","").strip().split())
                
                    if "NR.REMESSA" in dados:
                        numero_documento = dados.replace("NR.REMESSA:","").strip().split()[0]
                        
                    if "NR. AUTENTICACAO:" in dados:
                        autenticacao = dados.replace("NR. AUTENTICACAO:","").strip()
                        
                lista_cliente.append(cliente)
                lista_beneficiario.append(beneficiario)
                lista_cnpj_beneficiario.append(cnpj_beneficiario)
                lista_data_pagamento.append(data_de_pagamento)
                lista_data_vencimento.append(data_de_vencimento)
                lista_valor_pagamento.append(valor_pagamento)
                lista_juros.append(valor_juros)
                lista_valor_total_pagamento.append(valor_total)
                lista_nosso_numero.append(nosso_numero)
                lista_numero_documento.append(numero_documento)
                lista_autenticacao.append(autenticacao)
                lista_tipo_documento.append(tipo_documento)
        
                    
            if j == "COMPROVANTE DE TRANSFERENCIA":
                

                cliente = ''
                beneficiario = ''
                cnpj_beneficiario = ''
                data_de_pagamento = ''
                data_de_vencimento = ''
                valor_pagamento = ''
                valor_juros = '0,00'
                valor_total = ''
                nosso_numero = ''
                numero_documento = ''
                autenticacao = ''
                tipo_documento = 'COMPROVANTE DE TRANSFERENCIA'

                
                for dados in lista_texto:
                    if "CLIENTE:" in dados:
                        cliente = dados.replace("CLIENTE:","").strip()
                        
                    if "TRANSFERIDO PARA:" in dados:
                        beneficiario = dados[dados.index(dados) + 1].replace("CLIENTE:","").strip()
                    
                    if "DATA DA TRANSFERENCIA" in dados:
                        data_de_pagamento = dados.replace("DATA DA TRANSFERENCIA","").strip()
                    
                    if "VALOR TOTAL" in dados:
                        valor_pagamento = dados.replace("VALOR TOTAL","").strip()
                        valor_total = dados.replace("VALOR TOTAL","").strip()
                    
                    if "NR.AUTENTICACAO" in dados:
                        autenticacao = dados.replace("NR.AUTENTICACAO","").strip()
                
                lista_cliente.append(cliente)
                lista_beneficiario.append(beneficiario)
                lista_cnpj_beneficiario.append(cnpj_beneficiario)
                lista_data_vencimento.append(data_de_vencimento)
                lista_data_pagamento.append(data_de_pagamento)
                lista_valor_pagamento.append(valor_pagamento)
                lista_juros.append(valor_juros)
                lista_valor_total_pagamento.append(valor_total)
                lista_nosso_numero.append(nosso_numero)
                lista_numero_documento.append(numero_documento)
                lista_autenticacao.append(autenticacao)
                lista_tipo_documento.append(tipo_documento)
        
    excel = {
        "Pagador" : lista_cliente,
        "Beneficiario" : lista_beneficiario,
        "CNPJ Beneficiario" : lista_cnpj_beneficiario,
        "Data de Pagamento" : lista_data_pagamento,
        "Data de Vencimento" : lista_data_vencimento,
        "Valor dos Juros" : lista_juros,
        "Valor do Pagamento" : lista_valor_pagamento,
        "Valor Total" : lista_valor_total_pagamento,
        "Nosso Numero" : lista_nosso_numero,
        "Numero do Documento" : lista_numero_documento,
        "Autenticação" : lista_autenticacao,
        "Tipo de Documento" : lista_tipo_documento
    }

    tabela = pandas.DataFrame(excel)
    tabela.to_excel(f"{MEDIA_ROOT}/{nome_arquivo}.xlsx",index=False)
