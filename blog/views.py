from django.shortcuts import render , HttpResponse , get_object_or_404
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def post_list(request):
    post_list = Post.objects.all().filter(status=Post.Status.PUBLISHED)
    paginator = Paginator(post_list , 2)
    pagenumber = request.GET.get('page',1)
    posts = paginator.page(pagenumber)
    context = { 'posts' : posts}
    return render(request , 'post\list.html' , context )

def post_detail(request , slug):
    post = get_object_or_404(Post , slug=slug , status=Post.Status.PUBLISHED)
    context = { 'post' : post}
    return render(request , 'post\detail.html' , context)
