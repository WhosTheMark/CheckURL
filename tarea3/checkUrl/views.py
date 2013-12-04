from django.shortcuts import render
from form import URLForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import urllib
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.

#AGREGAR UTF-8 !!

#Puede que valide el url antes de chequear (URLValidator)
def home(request):
   args = {}
   args.update(csrf(request))
   if request.POST:
      form = URLForm(request.POST)
      if form.is_valid():
         validate = URLValidator()
         direccion = form.cleaned_data['direccion']
         try:
            validate(direccion)
         except ValidationError, e:
            direccion = "http://" + direccion
         try:
            print urllib.urlopen(direccion).getcode()
            args['resultado'] = "La pagina funciona!"
         except IOError, e:
            args['resultado'] = "Al parecer la pagina esta caida :("
         return render(request, 'checkUrl/result.html', args)
         # Falta chequear si el url funciona o no.
   form = URLForm()
   args['form'] = form
   return render(request, 'checkUrl/index.html', args) #por ahora sin el contexto diccionario.
