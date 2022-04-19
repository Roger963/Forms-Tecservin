from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormularioForm

# Create your views here.
def form_generali(request):
    form = FormularioForm(request.POST, request.FILES)
    print(request.FILES)
    return render(request,'generali/formgenerali.html',{'form':form})