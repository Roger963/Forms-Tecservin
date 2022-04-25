from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormularioForm

# Create your views here.
def form_generali(request):
    if request.POST:
    #if (request.method == 'POST' ):
        form = FormularioForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(form_generali)
    return render(request,'./generali/formgenerali.html',{'form':FormularioForm})