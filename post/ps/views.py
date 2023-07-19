from django.shortcuts import render, redirect
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


