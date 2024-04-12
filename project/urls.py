"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#CLIENTE PEDE <-- SERVIDOR RESPONDE
#HTPP RESQUEST <-- HTTP RESPONSE


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),#/
    path('recipes/', include('recipes.urls')) #dominio.com/recipes/
]

#Inspesionar do navegador e Network para visualizar (https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)
#Os códigos de status de resposta HTTP indicam se uma solicitação HTTP específica foi concluída com êxito. As respostas são agrupadas em cinco classes:
# Respostas Informativas (100 – 199)
# Respostas bem-sucedidas (200 – 299)
# Mensagens de redirecionamento (300 – 399)
# Respostas de erro do cliente (400 – 499)
# Respostas de erro do servidor (500 – 599)