"""PrimeiroSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from core.views import olamundo #importando do core
from core.views import disciplina
#from core.views import home
from core.views import minha_idade
from core.views import meu_nome
from core.views import minha_nota
from core.views import cadastro
from core.views import pagina1
from core.views import pagina2
from core.views import home, contato

urlpatterns = [ #As urls são colocadas aqui, com 2 parametros, o nome da url e a viw que o usuario vai acessar
  #  path ('inicio', home),
    path ('nota/<str:nota>/', minha_nota),
    path ('nome/<str:nome>/', meu_nome), #nome
    path ('idade/<int:idade>', minha_idade), #inteiro
    path ('cadastro/<str:nome>/<int:idade>/', cadastro),
    path ('disciplina/', disciplina),
    path ('ola/', olamundo),
    path ('admin/', admin.site.urls),
    path ('pagina1/', pagina1),

    #nome é na URL     como esta em views
    path ('pagina2/', pagina2),
    path ('contato/', contato, name='contato'),
     path ('', home), #Não tem nada entre as aspas pois essa sera a pagina inicial, acessado por "localhoste:8000"
]
