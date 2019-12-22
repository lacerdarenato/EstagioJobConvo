from django.conf.urls import  include, url
from django.contrib.auth.views import login, logout
from est.accounts.views import register, telaCandidato

urlpatterns = [
     url(r'^entrar/$', login, name='login'),
     url(r'^sair/$', logout, name='logout'),
     url(r'^$', register, name='register'),
     url(r'^$', telaCandidato, name='telaCandidato'),
]