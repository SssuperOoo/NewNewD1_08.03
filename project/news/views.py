from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm
from django.shortcuts import redirect, reverse, HttpResponseRedirect, render

class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-post_time'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    paginate_by = 10
class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

class PostSearch(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'news_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

class ArticleCreate(CreateView):
    model = Post
    template_name = 'article_create.html'
    form_class = PostForm
    # success_url = reverse_lazy('post_detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_type = 'AR'  # Задаем тип записи как "статья"
        return super().form_valid(form)

