from rest_framework import serializers
from .models import *
class SnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model=SnippetModel
        # 给用户展示的数据
        fields=('title','code','lineos')
#    fields='__all__'将数据库所有的字段都返回



