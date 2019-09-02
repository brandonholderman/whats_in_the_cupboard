# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import SearchSerializer
from .sample_data import MOCK_DATA
from .models import Search
import requests
import os


class SearchView(generics.ListAPIView):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['label']


class HomeView(TemplateView):
    """
    Home View Class.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class SearchView(mixins.ListAPIMixin):

#     serializer_class = SearchSerializer

#     def get(self, request):
#         response = requests.get(MOCK_DATA)
#         if response.ok:
#             return response
#         else:
#             return None


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

# def home(request):
    # ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    # response = requests.get(
    #     'https://nasaapidimasv1.p.rapidapi.com/getAsteroidStats')
    # nasadata = response.json()
    # return render(request, 'home.html', {
        # 'ip': nasadata['ip'],
        # 'country': nasadata['country_name'],
        # 'latitude': nasadata['latitude'],
        # 'longitude': nasadata['longitude'],
        # 'api_key': os.environ.get('API_KEY', '')
# })

# Create your views here.



