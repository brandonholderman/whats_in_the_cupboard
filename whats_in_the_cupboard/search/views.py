# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, ListView
from django.shortcuts import render


# Create your views here.
class HomeView(TemplateView):
    """
    Home View Class.
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['latest_articles'] = Article.objects.all()[:5]

        return context
