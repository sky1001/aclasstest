from django.shortcuts import render

# Create your views here.
from django.views import View


class mixin_test(View):
       def get(self,request):
           return