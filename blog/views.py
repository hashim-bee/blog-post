from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
# Create your views here.
from . models import *

def Home(request):
    return render(request,'blog/index.html')

class createpost(CreateView):
    model = blogpost
    fields = ['title', 'content']
    template_name = 'blog/create-post.html'
    success_url = reverse_lazy('home')

class listPosts(ListView):
    model = blogpost
    context_object_name = 'posts'
    template_name = 'blog/list-post.html'
