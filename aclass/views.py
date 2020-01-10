from django.shortcuts import render

# Create your views here.
from django.views import View


class aclass(View):
    # 发送ｇｅｔ请求时进入额包
    def get(self,request):
        content ={
            'city':'beijiang'
        }
        print('get请求')
        return render(request,'index.html',content)
    def post(self,request):
        content = {
            'city':'邯郸'
        }
        print('ｐｏｓｔ请求')
        return render(request,'index.html',content)