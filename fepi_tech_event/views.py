from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fepi(request):
    return render(request, 'index.html')

def root_view(request):
    return HttpResponse("Estamos na Raiz, porta 8000")