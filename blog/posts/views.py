from django.shortcuts import render
from .models import Post
# Create your views here.
posts = Post.objects.all()
def index(request):
    return render(request,"index.html",{'posts': posts})
def post(request,pk):
    post =Post.objects.get(id=pk)
    return render(request,"post.html",{'post': post})