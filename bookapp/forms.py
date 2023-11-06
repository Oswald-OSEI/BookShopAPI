from django import forms
from .models import Books, Authors, Genre


class BookForm(forms.ModelForm):
    
    class Meta:
         model = Books
         fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['uploader'].widget.attrs['hidden']=True

class AuthorsForm(forms.ModelForm):
  
  class Meta:
      model = Authors
      fields = "__all__"
    
   
class GenreForm(forms.ModelForm):
    
    class Meta:
        model = Genre
        fields = "__all__"   