from django.shortcuts import render
from django.contrib import messages


def homepage(request):
    return render(request, 'index.html')








