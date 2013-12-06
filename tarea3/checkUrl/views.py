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
            args['result'] = "Wohoo! The website works! \nOh, but... Maybe your computer has something wrong...?"
         except IOError, e:
            args['result'] = "Aww... the website is down );"
         except ValidationError, e:
            args['result'] = "Hmmm... I think this is not a valid URL..."
         return render(request, 'checkUrl/result.html', args)

   form = URLForm()
   args['form'] = form
   return render(request, 'checkUrl/index.html', args) #por ahora sin el contexto diccionario.
