from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm 

def accounts(request):
    template_name = 'accounts/conta.html'
    return render(request, template_name)

@login_required
def telaCandidato(request):
    template_name = 'accounts/telaCandidato.html'
    return render(request, template_name)

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
