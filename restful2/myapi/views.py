from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .models import *
from django.http import HttpResponse,JsonResponse
from .serializer import *
import json

# Create your views here.
@api_view(['GET','POST'])
def index_views(request):
    if request.method=='GET':
        meizis = SnippetModel.objects.all()
        # http: // 127.0.0.1:8000 / getlist?limit = 20
        # http: // 127.0.0.1:8000 / getlist?limit = 20 & offset = 20
        # http: // 127.0.0.1:8000 / getlist?limit = 20 & offset = 40
        # 根据url参数 获取分页数据
        obj = StandardResultSetPagination()
        page_list = obj.paginate_queryset(meizis, request)
        # 对数据序列化 普通序列化 显示的只是数据
        ser = SnippetSerializers(page_list, many=True)  # 多个many=True # instance：把对象序列化
        response = obj.get_paginated_response(ser.data)
        return response
        # 从里面表中取出所有记录
        # all_data=SnippetModel.objects.values('title','code')
        # page_obj=page_clas()
        # page_list=page_clas.paginate_queryset(all_data,request.GET.get('limit'),request.GET.get('offset'))
        #
        # # 对所有对象进行序列化，转换为json格式的数据
        # show_data=SnippetSerializers(page_list,many=True)
        # return page_obj.get_paginated_response(show_data)
        # 展示为json格式的数据
        # return JsonResponse(show_data.data,safe=False)
    if request.method=='POST':
        try:
            # 拿到json格式的数据
            request_jilu=request.body

            #下面的2步是用于将json格式的数据进行转换为字典
            request_encode=request_jilu.decode()
            request_json=json.loads(request_encode)
        except:
            return JsonResponse(error_return("非法json格式",8000))
        # 将其转换为表里面的那种格式，反序列化
        try:
            jilu=SnippetSerializers(data=request_json)
            if jilu.is_valid():
                jilu.save()
                return JsonResponse(jilu.data)
            else:
                return HttpResponse(status=404)
        except:
            return JsonResponse(error_return("系统错误",8001))

@api_view(['GET','PUT','DELETE'])
def users_detail(request,id):
    try:
        one_data=SnippetModel.objects.get(id=id)
    except:
        return JsonResponse(error_return(8002,'非法id'))


    if request.method=='GET':
        try:
            serializers_obj = SnippetSerializers(one_data)
            return JsonResponse(serializers_obj.data)
        except:
            return HttpResponse(status=400)
    if request.method=='PUT':
        try:
            request_data=request.body.decode()
            print('获得的是2',request_data)
            print('获得的是',request.body)
            request_json=json.loads(request_data)
            print('这个是',request_json)
        except:
            return JsonResponse(error_return("非法json格式", 8000))
        obj_put=SnippetSerializers(one_data,data=request_json)
        if obj_put.is_valid():
            obj_put.save()
            print('6666')
            print(obj_put.data)
            return JsonResponse(obj_put.data)
        return JsonResponse(error_return(8003,"系统错误2"),status=404)
    if request.method=='DELETE':
        one_data.delete()
        return HttpResponse(status=200)

def error_return(msg,code):
    the_return={
        "code":code,
        "msg":msg,
        "results":[]
    }
    return the_return
