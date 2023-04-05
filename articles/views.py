
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy
from .models import Article, Comment



# Create your views here.
# This view is to sort User articles alone
class MyArticlesView(LoginRequiredMixin, ListView):  
    template_name = 'my_view.html'

    def get_queryset(self):
        querryset = Article.objects.filter(author=self.request.user).order_by('-id')
        return querryset


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article_list.html'

    def test_func(self): # adds the user authomatically
        obj = self.get_object()
        return obj.author == self.request.user

    def get_queryset(self):
        queryset = Article.objects.all()
        queryset = queryset.order_by('-id')  # this line enables descending order
        return queryset

class ArticleDetailView(LoginRequiredMixin, DetailView): # new
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)

    # This function enables the author to be added automatically...
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView): # new
    model = Article
    fields = ('title', 'body',) 
    template_name = 'article_edit.html'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ('comment',)

    # This function enables the author to be added automatically...
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['article_id']) # the new code
        return super().form_valid(form)
