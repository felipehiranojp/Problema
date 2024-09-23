from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def pagina1(request):
    return render(request, 'pagina1.html')

