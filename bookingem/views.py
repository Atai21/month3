from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from . import models, forms

class BookListView(ListView):
    template_name = 'books/book_list.html'
    queryset = models.Books.objects.all()

    def get_queryset(self):
        return models.Books.objects.all()

class BookCreateView(CreateView):
    template_name = 'books/book_create.html'
    form_class = forms.BookForm
    success_url = '/'
    queryset = models.Books.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)


class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

class BookUpdateView(UpdateView):
    template_name = 'books/book_create.html'
    form_class = forms.BookForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('books:book-list')


class BookDeleteView(DeleteView):
    template_name = 'books/book_delete.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def get_success_url(self):
        return reverse('books:book-list')

class CommentCreateView(CreateView):
    template_name = 'books/book_detail.html'
    form_class = forms.CommentForm
    queryset = models.Comment.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)
