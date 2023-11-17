import PyPDF2
from core.settings import MEDIA_ROOT
import pandas as pd
    
    
def gera_excel_sicoob(arquivo,nome_arquivo):
    arquivo = PyPDF2.PdfReader(arquivo)
    total_paginas = len(arquivo.pages)

    lista_pagador = []
    lista_beneficiario = []
    lista_cnpj_beneficiario = []
    lista_data_pagamento = []
    lista_data_vencimento = []
    lista_valor_documento = []
    lista_descontos_abatimentos = []
    lista_outros_acrescimos = []
    lista_valor_pago = []
    lista_nosso_numero = []
    lista_autenticacao = []
    lista_tipo_documento = []

    for i in range(total_paginas):
        texto_extraido = arquivo.pages[i].extract_text().split("Linha digitável:")
        for j in range(len(texto_extraido)):
            
            
            if j == 0:
                pass
            else:
                nosso_numero = ''
                pagador = ''
                beneficiario = ''
                cnpj_beneficiario = ''
                data_pagamento = ''
                data_vencimento = ''
                valor_documento = ''
                descontos_abatimentos = ''
                outros_acrescimos = ''
                valor_pago = ''
                autenticacao = ''
                tipo_documento = ''
                
                
                parte_folha = texto_extraido[j].split("\n")
                for parte in parte_folha:
                    
                    if "Nosso Número" in parte:
                        nosso_numero = parte.replace("Nosso Número:","").strip()
                    
                    if "Nome/Razão Social do Pagador:" in parte:
                        pagador = parte.replace("Nome/Razão Social do Pagador:","").strip()
                    
                    if "Nome/Razão Social do Beneficiário:" in parte:
                        beneficiario = parte.replace("Nome/Razão Social do Beneficiário:","").strip()
                    
                    if "CPF/CNPJ Beneficiário:" in parte:
                        cnpj_beneficiario = parte.replace("CPF/CNPJ Beneficiário:","").strip()
                    
                    if "Data Pagamento:" in parte:
                        data_pagamento = parte.replace("Data Pagamento:","").strip()
                    
                    if "Data Vencimento: " in parte:
                        data_vencimento = parte.replace("Data Vencimento: ","").strip()
                        
                    if "Valor Documento: " in parte:
                        valor_documento = parte.replace("Valor Documento:","").strip()
                        
                    if "(-) Desconto / Abatimento:" in parte:
                        descontos_abatimentos = parte.replace("(-) Desconto / Abatimento:","").strip()
                        
                    if "(+) Outros acréscimos:" in parte:
                        outros_acrescimos = parte.replace("(+) Outros acréscimos:","").strip()
                        
                    if "Valor Pago:" in parte:
                        valor_pago = parte.replace("Valor Pago:","").strip()
                        
                    if "Autenticação:" in parte:
                        autenticacao = parte.replace("Autenticação:","").strip()
                    
                    if "Tipo Documento:" in parte:
                        tipo_documento = parte.replace("Tipo Documento:","").strip()
                        
                lista_nosso_numero.append(nosso_numero)
                lista_pagador.append(pagador)
                lista_beneficiario.append(beneficiario)
                lista_cnpj_beneficiario.append(cnpj_beneficiario)
                lista_data_pagamento.append(data_pagamento)
                lista_data_vencimento.append(data_vencimento)
                lista_valor_documento.append(valor_documento)
                lista_descontos_abatimentos.append(descontos_abatimentos)
                lista_outros_acrescimos.append(outros_acrescimos)
                lista_valor_pago.append(valor_pago)
                lista_autenticacao.append(autenticacao)
                lista_tipo_documento.append(tipo_documento)

                excel = {
                        "Pagador": lista_pagador,
                        "Beneficiario": lista_beneficiario,
                        "CNPJ Beneficiario" : lista_cnpj_beneficiario,
                        "Data Pagamento": lista_data_pagamento,
                        "Data Vencimento": lista_data_vencimento,
                        "Valor Documento": lista_valor_documento,
                        "Descontos/Abatimentos ": lista_descontos_abatimentos,
                        "Outros Acrescimos": lista_outros_acrescimos,
                        "Valor Pago": lista_valor_pago,
                        "Nosso Número": lista_nosso_numero,
                        "Autenticação": lista_autenticacao,
                        "Tipo de Documento" : lista_tipo_documento
                }
                
                arquivo_excel = pd.DataFrame(excel)
                arquivo_excel.to_excel(f"{MEDIA_ROOT}/{nome_arquivo}.xlsx",index=False)