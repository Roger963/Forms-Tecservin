from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from django.contrib import messages
from .models import survey_page


def index(request):
    return render(request, 'survey.html')

def detail(request, survey_page_id):
    return HttpResponse(f"Pagina Resultado {survey_page_id}")

def results(request, survey_page_id):
    return render(request, 'detail.html')

def vote(request, survey_page_id):
    return HttpResponse(f"vote page {survey_page_id}")
