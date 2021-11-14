from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'

class TreePageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/tree.html'

class PageView(LoginRequiredMixin, TemplateView):
    model = Page
    template_name = 'pages/graham_page.html'

class KPageView(LoginRequiredMixin, TemplateView):
    model = Page
    template_name = 'pages/karin_page.html'


