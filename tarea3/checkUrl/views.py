# -*- coding: utf-8 -*- 

from django.shortcuts import render
from form import URLForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import urllib
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.

def home(request):
   args = {}
   args.update(csrf(request))
   if request.POST:
      form = URLForm(request.POST)
      if form.is_valid():
         validate = URLValidator()
         address = form.cleaned_data['direccion']
         try:
            validate(address)
         except ValidationError, e:
            address = "http://" + address
         try:
            validate(address)
            code = urllib.urlopen(address).getcode()
            args['result'] = "La página funciona!"
         except IOError, e:
            args['result'] = "Al parecer la página esta caída :("
         except ValidationError, e:
            args['result'] = "Hmmm.. creo que esto no es un URL válido"
         return render(request, 'checkUrl/result.html', args)

   form = URLForm()
   args['form'] = form
   return render(request, 'checkUrl/index.html', args) #por ahora sin el contexto diccionario.
