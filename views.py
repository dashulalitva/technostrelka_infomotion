from dataclasses import field
from lib2to3.fixes.fix_input import context
from tkinter.font import names

from django.contrib.admin.templatetags.admin_list import results
from django.shortcuts import render, redirect
from django.views.generic import ListView

from main.models import Films
import sqlite3
from .forms import FilmsForm
import os
from django.views.generic.base import View

def index(request):
    image_dir = os.path.join('films')
    name_img = os.listdir(image_dir)
    full_name_img = list()
    for i in name_img:
        chenge = '/films/' + i
        full_name_img.append(chenge)
    film = Films.objects.all()
    return render(request, 'main/index.html', {'film_list': film})

def about(request):
    return render(request, 'main/about.html')

def search(request):
    if request.method == 'POST':
        query_name = request.POST.get('name', None)
        if query_name:
            results = Films.objects.filter(name__contains=query_name)
            return render(request, 'main/base.html', {'results': results})
    return render(request, 'main/base.html')


