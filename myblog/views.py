from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from .models import Post
from .forms import SigUpForm, SignInForm, CreateArticleForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic.edit import FormView
from django.views.generic import CreateView, DetailView
from django.urls import reverse
from django.utils import timezone


def create_article(request):
    error = ''
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма заполнена неверно."
    else:
        form = CreateArticleForm()
    context = {'forms': form, 'error': error}
    return render(request, 'myblog/write_article.html', context)


class WriteArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/write_article.html')


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/about.html')


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.get_queryset().order_by('-created_at')
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/index.html', context={
            'page_obj': page_obj
        })


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'myblog/post_detail.html', context={'post': post})


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'myblog/signup.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'myblog/signin.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signin.html', context={'form': form})


class SearchResultView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })


# class SearchResultView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'myblog/search.html', context={
#             'title': 'Поиск'
#         })


class WriteArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/write_article.html')





