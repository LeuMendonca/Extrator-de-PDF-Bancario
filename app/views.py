from django.shortcuts import render
from django.http import HttpResponse
from app.funcoes.exporta_excel_banco_brasil import gera_excel_bb
from app.funcoes.exporta_excel_bradesco import gera_excel_bradesco
from app.funcoes.exporta_excel_sicoob import gera_excel_sicoob
from app.funcoes.exporta_excel_itau import gera_excel_itau
from app.funcoes.exporta_excel_santander import gera_excel_santander
from django.conf import settings
import PyPDF2
import os
from datetime import datetime

def index(request):
    if request.method == 'POST':
        arquivo = request.FILES['pdf_file']
        nome_arquivo = str(arquivo).lower().replace(".pdf","") + f"-{datetime.today().strftime('%d-%m-%Y')}"

        if "BANCO  DO  BRASIL" or "BANCO DO BRASIL" or "Consultas - Emissão de comprovantes" in PyPDF2.PdfReader(arquivo).pages[0].extract_text().split()[0]:
            gera_excel_bb(arquivo,nome_arquivo)
        
        if "Alô Bradesco" in PyPDF2.PdfReader(arquivo).pages[0].extract_text():
            gera_excel_bradesco(arquivo,nome_arquivo)
            
        if "www.itau.com.br" in PyPDF2.PdfReader(arquivo).pages[0].extract_text():
            gera_excel_itau(arquivo,nome_arquivo)

        if "SICOOB - Sistema de Cooperativas de Crédito do Brasil" in PyPDF2.PdfReader(arquivo).pages[0].extract_text():
            gera_excel_sicoob(arquivo,nome_arquivo)
        
        if "Central de Atendimento Santander Empresarial" in PyPDF2.PdfReader(arquivo).pages[0].extract_text():
            gera_excel_santander(arquivo,nome_arquivo)
        
        caminho = nome_arquivo + ".xlsx"
        caminho = os.path.join(settings.MEDIA_ROOT,caminho)
        if os.path.exists(caminho):
            with open(caminho,'rb') as fh:
                response = HttpResponse(fh.read(),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'ubkube;filename=' + os.path.basename(caminho)
            fh.close()
            os.remove(caminho)
            return response
    return render(request,"app/index.html",)

def combinar_pdf(request):
    if request.method == 'POST':
        arquivo_merge = request.FILES.getlist('pdf_merge')
        arquivo_combinado = PyPDF2.PdfMerger()
       
        for arq in arquivo_merge:
            arquivo_combinado.append(arq)
        
        data_hoje = datetime.today().strftime('%d-%m-%Y')
        
        nome_arquivo_gerado = f"pdf_combinado_{data_hoje}.pdf"
        caminho_arquivo_gerado = os.path.join(settings.MEDIA_ROOT,nome_arquivo_gerado)

        arquivo_combinado.write(caminho_arquivo_gerado)

        if os.path.exists(caminho_arquivo_gerado):
            with open(caminho_arquivo_gerado,'rb') as fh:
                response = HttpResponse(fh.read(),content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=' + os.path.basename(caminho_arquivo_gerado)
            fh.close()
            os.remove(caminho_arquivo_gerado)
            return response

        

    return render(request,"app/index.html",)


