# 定义中间间
def my_middleware(get_response):
    print('init被调用')
    def middleware(request):
        print('befort 之前被调用')
        response=get_response(request)
        print('after之后执行')
        return response
    return middleware
def my_middleware1(get_response):
    print('init1被调用')
    def middleware(request):
        print('befort1 之前调用')
        response =  get_response(request)
        print('after1之后执行')
        return response
    return middleware