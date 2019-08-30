# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
import requests
import os
# from mixins import ListModelMixin, CreateModelMixin, GenericAPIView


# Create your views here.
# class HomeView(TemplateView):
#     """
#     Home View Class.
#     """
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # context['latest_articles'] = Article.objects.all()[:5]
#         ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
#         response = requests.get('http://freegeoip.net/json/%s' % ip_address)
#         geodata = response.json()
#         return render(context, 'core/home.html', {
#             'ip': geodata['ip'],
#             'country': geodata['country_name']
#         })

# def home(request):
#     ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
#     response = requests.get('http://freegeoip.net/json/%s' % ip_address)
#     geodata = response.json()
#     return render(request, 'core/home.html', {
#         'ip': geodata['ip'],
#         'country': geodata['country_name']
#     })


def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': os.environ.get('API_KEY', '')
    })

# class PostCollection(ListModelMixin,
#                              CreateModelMixin,
#                              GenericAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#         return context
