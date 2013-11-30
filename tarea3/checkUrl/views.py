from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'checkUrl/index.html') #por ahora sin el contexto diccionario.