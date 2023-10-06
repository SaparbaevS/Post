from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from ps.forms import PostForm, PostModelForm
from ps.models import Post

def start_page(request):
    context = {"blogs": Post.objects.all()}
    return render(request, "index.html", context=context)


def show_post(request, post_id):
    context = {"blog": Post.objects.get(pk=post_id)}
    return render(request, "show.html", context=context)


def add_post(request):

    if request.method == "POST":
        post = PostModelForm(request.POST)
        if post.is_valid():
            post.save()

            return redirect("start_page")

    else:
        post = PostModelForm()
    context = {"post": post}

    return render(request, "add_post.html", context)


def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_page')
        else:
            render(request, 'register.html', {'form': form})
    context = {'form': form}

    return render(request, 'register.html', context)



class LoginPageView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start_page')

class LogoutPageView(LogoutView):
    next_page = reverse_lazy('login')