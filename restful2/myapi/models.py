from django.db import models

# Create your models here.
from rest_framework.pagination import LimitOffsetPagination


class SnippetModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=200,blank=True,default='')
    code=models.TextField()
    lineos=models.BooleanField(default=False)
    style=models.CharField(default='friendly',max_length=100)
    class Meta:
        db_table='Snippt'
        verbose_name='别名'
        verbose_name_plural=verbose_name
        ordering=('created',)
    # def __str__(self):
    #     return self.created
class StandardResultSetPagination(LimitOffsetPagination):
 # 默认每页显示的条数
 default_limit = 20
 # url 中传入的显示数据条数的参数
 limit_query_param = 'limit'
 # url中传入的数据位置的参数
 offset_query_param = 'offset'
 # 最大每页显示条数
 max_limit = None


