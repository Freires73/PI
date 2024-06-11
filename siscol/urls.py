from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('reciclagem/', include('reciclagem.urls')),
    path('pontocoleta/', include('pontocoleta.urls')),
    path('vendas/', include('vendas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('plataforma/', include('plataforma.urls')),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)