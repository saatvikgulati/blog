from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post 
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
'''data=[
    {
    'title':'post1',
    'author':'Saatvik',
    'date_posted':'October 25th, 2019'
    },
    {
    'title':'post2',
    'author':'Harshal',
    'date_posted':'October 26th, 2019'
    }
]'''
def home(request):
    #context={'data':data}
    context={
        'data':Post.objects.all()
    }
    if(request.method=='GET'):
        query=request.GET.get("q")
        qs=Post.objects.all()
        if query is not None:
            qs=qs.filter(title__icontains=query)
            context={
                'data':qs
            }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
def contact(request):
    return HttpResponse('<h1>Contact page</h1>')
#class based views
class PostListView(ListView): #default object name is object_list
    model=Post
    template_name='blog/home.html'
    context_object_name='data'
    ordering=['-date_posted']
    paginate_by=2

class UserPostListView(ListView): #default object name is object_list
    model=Post
    template_name='blog/home.html'
    context_object_name='data'
    #ordering=['-date_posted']
    paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

#class based view post detail
#cannot use decorators with class based views
class PostDetailView(DetailView): #default object name is object
    model=Post
    #<app>/<model>_<viewType>.html

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    #template this class will look for is post_create
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    #template this class will look for is post_create
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/blog/' #not a var it is an underlining function
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False

def search(request):
    context={
        'data':Post.objects.all()
    }
    return render(request,'blog/search.html',context)