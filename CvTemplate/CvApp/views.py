from django.shortcuts import render
from django.http import request


def index_view(request):
    return render(request, 'website/index.html')
