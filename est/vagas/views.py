from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    vaga = vagas.objects.all()
    template_name = 'vagas/index.html'
    context = { 'vagas': vaga}

    return render(request, template_name, context)

def enrollment(request, slug):
    vaga = get_object_or_404(vagas, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, vagas=vaga
    )

    if created: 
        enrollment.active()
        
    return redirect('telaCandidato')

