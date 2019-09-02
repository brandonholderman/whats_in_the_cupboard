# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import SearchSerializer
from .sample_data import MOCK_DATA
from .models import Search
import requests
import os


# class SearchView(viewsets.ModelViewSet):
#     serializer_class = SearchSerializer

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         queryset = Search.objects.all()


class HomeView(TemplateView):
    """
    Home View Class.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchView(mixins.ListModelMixin):

    serializer_class = SearchSerializer

    def get_queryset(self):
        response = requests.get(MOCK_DATA)
        if response.ok:
            return response
        else:
            return None


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


# def home(request):
#     url = "https://nasaapidimasv1.p.rapidapi.com/getAsteroidStats"
#     payload = ""
#     headers = {
#         'x-rapidapi-host': "NasaAPIdimasV1.p.rapidapi.com",
#         'x-rapidapi-key': "38c11f5b86msh745fb6e602101e6p172f76jsn44947788b021",
#         'content-type': "application/x-www-form-urlencoded"
#     }

#     response = requests.request("POST", url, data=payload, headers=headers)

#     print(response.text)

# Create your views here.



