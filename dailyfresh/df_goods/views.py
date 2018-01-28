#coding:utf8
from django.shortcuts import render
from models import *
# Create your views here.

def index(request):
    #查询各个商品分类中最新和最热的4条
    typelist = TypeInfo.objects.all()
    #新鲜水果分类下最新的4种商品
    type0 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    #新鲜水果分类下点击量最高的4种商品
    type01 = typelist[0].goodinfo_set.order_by('-gclick')[0:4]
    #海鲜水产分类下最新的4种商品
    type1 = typelist[1].goodinfo_set.order_by('-id')[0:4]
    #海鲜水产分类下点击量最高的4种商品
    type11 = typelist[1].goodinfo_set.order_by('-gclick')[0:4]
    #猪牛羊肉分类下最新的4种商品
    type2 = typelist[2].goodinfo_set.order_by('-id')[0:4]
    #猪牛羊肉分类下点击量最高的4种商品
    type21 = typelist[2].goodinfo_set.order_by('-gclick')[0:4]
    #禽类蛋品分类下最新的4种商品
    type3 = typelist[3].goodinfo_set.order_by('-id')[0:4]
    #禽类蛋品分类下点击量最高的4种商品
    type31 = typelist[3].goodinfo_set.order_by('-gclick')[0:4]
    #新鲜蔬菜分类下最新的4种商品
    type4 = typelist[4].goodinfo_set.order_by('-id')[0:4]
    #新鲜蔬菜分类下点击量最高的4种商品
    type41 = typelist[4].goodinfo_set.order_by('-gclick')[0:4]
    #速冻食品分类下最新的4种商品
    type5 = typelist[5].goodinfo_set.order_by('-id')[0:4]
    #速冻食品分类下点击量最高的4种商品
    type51 = typelist[5].goodinfo_set.order_by('-gclick')[0:4]
    context = {
        'title': '首页','guest_cart': 1,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(request, 'df_goods/index.html', context)