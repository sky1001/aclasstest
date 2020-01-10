from django.shortcuts import render

# Create your views here.
# 创建类视图函数
from django.utils.decorators import method_decorator
from django.views import View
# 定义　装饰起
def my_decorator(func):
    def inner(request,**kwargs):
        print('装饰器被调用了')
        print('调用路径{}'.format(request.path))
        return func(request,**kwargs)
    return inner
# 定义类视图
# @method_decorator(my_decorator,name='dispatch')
class classdecorator(View):
    def get(self,request):
        content={
            'name':'zhangsan'
        }
        return render(request,'text.html',content)

