from django.db import models

# Create your models here.

class ArquivoPDF(models.Model):
    arquivo = models.FileField(upload_to='pdfs/')
    