from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('nome','nome') 
#name is from model field
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ('titulo', 'categoria', 'autor', 'corpo', 'imagem', 'arquivo', 'youtube')

#for bootstrap
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'}), #css
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'users_id', 'type': 'hidden'}), #dropdown
            'corpo': forms.Textarea(attrs={'class': 'form-control'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PostSearchForm(forms.Form):
    q = forms.CharField()
    c = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('nome'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = ''
        self.fields['c'].required = False
        self.fields['c'].label = 'Categoria'
        self.fields['q'].label = 'Pesquisar por'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})