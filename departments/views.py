from django.shortcuts import render
from django.views.generic import ListView
from django.views import  View

class HomePageView(View):
    def get(self, request):

        return render(request, 'dashboard.html')


