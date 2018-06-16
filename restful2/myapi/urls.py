from django.conf.urls import url
from .views import *
# 那么year,month将会对应views传递过来的year,month的值，而后面紧跟的则代表正则表达匹配的模式。
#    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
# http;//127.0.0.1:8000/artices/1111/22,这样传的参数是year=1111,month=22,相应的函数参数是year,name
#  那么year,month将会对应views传递过来的year,month的值，而后面紧跟的则代表正则表达匹配的模式。
# 语法为： (?P<name>pattern)， name 可以理解为所要传递的参数的名称，pattern代表所要匹配的模式
urlpatterns=[
    url(r'^index/$',index_views),
    url(r'^(?P<id>[0-9]+)/$',users_detail)
]