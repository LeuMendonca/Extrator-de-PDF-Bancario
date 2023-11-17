from django.urls import path
from .views import index,combinar_pdf
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/',index,name='index'),
    path('merge/',combinar_pdf,name="merge")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
