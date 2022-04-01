from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from django.contrib import messages
# from .models import Hospital


def index(request):
    return render(request, 'survey.html')
