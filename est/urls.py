from django.conf.urls import  include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from est.accounts.views import accounts, register, telaCandidato
from est.core.views import home
from est.core.views import contact
from est.vagas.views import index, Enrollment 





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^entrar/$', login, name='login'),
    url(r'^sair/$', logout, name='logout'),
    url(r'^conta/', accounts, name='accounts'),
    url(r'^contato/', contact, name='contact' ),
    url(r'^vagas/', index, name='vagas'),
    url(r'^cadastrar/', register, name='register'),
    url(r'^painel/', telaCandidato, name='telaCandidato'),
    url(r'^inscrever/', Enrollment, name='enrollment'),
]    