#coding:utf8
from django.db import models
#文本编辑器
from tinymce.models import HTMLField
# Create your models here.

#商品类别模型
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


#商品模型
class GoodInfo(models.Model):
    #商品名陈
    gtitle = models.CharField(max_length=20)
    #商品图片
    gpic = models.ImageField(upload_to='df_goods')
    #价格
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    #单位
    gunit = models.CharField(max_length=20)
    #点击量
    gclick = models.IntegerField()
    #简介
    gjianjie = models.CharField(max_length=100)
    #库存
    gkucun = models.IntegerField()
    #商品详情
    gcontent = HTMLField()
    #商品分类
    gtype = models.ForeignKey(TypeInfo)
    #推荐
    # gadv = models.BooleanField(default=False)
    def __str__(self):
        return self.gtitle.encode('utf-8')
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'