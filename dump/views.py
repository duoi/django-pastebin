from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
from django.utils.crypto import get_random_string

# Create your views here.
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.unique_key = get_random_string(length=4, allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            post.save()
            return redirect('dump.views.post_detail', post.unique_key)
    else:
        form = PostForm()
    return render(request, 'dump/new_post.html', {'form': form})

def post_detail(request, unique_key):
    post = get_object_or_404(Post, unique_key=unique_key)
    return render(request, 'dump/post_detail.html', {'post': post})
