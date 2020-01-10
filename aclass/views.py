from django.shortcuts import render

# Create your views here.
from django.views import View


class aclass(View):
    def get(self,request):
        content ={
            'city':'beijiang'
        }
        return render(request,'index.html',content)
    def post(self,request):
        return