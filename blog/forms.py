from django import forms
from .models import Comentario, Post

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor']