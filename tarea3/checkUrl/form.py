from django import forms
from URLToCheck import URLToCheck

class URLForm(forms.ModelForm):
   
   class Meta:
      model = URLToCheck