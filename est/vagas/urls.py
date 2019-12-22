from django.conf.urls import  include, url
from est.vagas.views import index, Enrollment

urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^(?P<slug>[\W_-/]+)/inscrever/$', Enrollment , name='enrollment') 
    
]
