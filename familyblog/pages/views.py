from django.views.generic import TemplateView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Page
from .forms import PageForm, PageEditForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class TreePageView(TemplateView):
    template_name = 'pages/tree.html'

class PageView(TemplateView):
    model = Page
    template_name = 'pages/graham_page.html'

class KPageView(TemplateView):
    model = Page
    template_name = 'pages/karin_page.html'


