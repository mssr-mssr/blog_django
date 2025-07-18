from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import FormularioComentario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
#from django import ListView

# Create your views here.
@login_required
def lista_posts(request):
	post = Post.objects.all().order_by
	return render(request, 'blog/lista_posts.html', {'posts':post})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()
    #return render(request, 'blog/detalle_post.html', {'post': post, 'comentarios': comentarios})

    if request.method == 'POST':
        form = FormularioComentario(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.save()
            form = FormularioComentario()
    else:
        form = FormularioComentario()
        
    return render(request, 'blog/detalle_post.html', {
        'post' : post,
        'comentarios' : comentarios,
        'form' : form
    })

'''
class ListaPostView(ListView):
    model = Post
    template_name = 'blog/lista_post_cbv.html'
    contex_object_name = 'posts'
'''

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login') 
    return render(request, 'blog/registro.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('lista_posts')
        else:
            return render(request, 'blog/login.html', {'error': 'Credenciales incorrectas'})
    
    return render(request, 'blog/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')
