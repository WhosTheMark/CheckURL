from django.shortcuts import render
from form import URLForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.

def home(request):
   if request.POST:
      form = URLForm(request.POST)
      return render(request, 'checkUrl/index.html') #Por ahora devuelve a la pagina inicial
      # Falta chequear si el url funciona o no.

   form = URLForm()
   args = {}
   args.update(csrf(request))
   args['form'] = form
   return render(request, 'checkUrl/index.html', args) #por ahora sin el contexto diccionario.