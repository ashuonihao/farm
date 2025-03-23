from django.db import models


class User(models.Model):
    SEX_CHOICE = (
        ('男','男'),
        ('女','女')
    )
    id = models.AutoField(primary_key=True,verbose_name='id')
    tel = models.CharField(max_length=64, verbose_name='手机号',null=True, blank=True)
    password = models.CharField(max_length=64, verbose_name='密码')
    username = models.CharField(max_length=64, verbose_name='姓名',null=False,blank=False, unique=True)
    sex = models.CharField(max_length=4, verbose_name='性别', choices=SEX_CHOICE, null=True, blank=True)
    address = models.CharField(max_length=128,verbose_name='地址',null=True,blank=True)
    avatar  = models.ImageField(upload_to='avatar/',verbose_name='用户头像',null=True,blank=True)
    class Meta:
        verbose_name = '用户管理'  # 定义在管理后台显示的名称
        verbose_name_plural = verbose_name  # 定义复数时的名称（去除复数的s）

    def __str__(self):
        return self.username

class Rice(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='id')

    sheng = models.CharField(max_length=128,verbose_name='省份')
    pzlx = models.CharField(max_length=128,verbose_name='品种名称')
    qbly = models.CharField(max_length=128,verbose_name='亲本来源')
    lx = models.CharField(max_length=128,verbose_name='类型')
    ycd = models.CharField(max_length=128,verbose_name='原产地')
    sdbh = models.CharField(max_length=128,verbose_name='审定编号')
    sdf = models.CharField(max_length=128,verbose_name='审定方')
    sdxh = models.CharField(max_length=128,verbose_name='审定序号')
    mb = models.CharField(max_length=128,verbose_name='母本')
    sdgs = models.CharField(max_length=128,verbose_name='审定公司')

    recordDate = models.DateField(verbose_name='发布日期')

    class Meta:
        verbose_name = '水稻管理'  # 定义在管理后台显示的名称
        verbose_name_plural = verbose_name  # 定义复数时的名称（去除复数的s）
        ordering = ['-recordDate']  # 排序


class Products(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='id')

    categoryName = models.CharField(max_length=128,verbose_name='分类')
    productName = models.CharField(max_length=128,verbose_name='品名')
    unit = models.CharField(max_length=128,verbose_name='单位')
    priceMax = models.FloatField(verbose_name='最高价')
    priceAvg = models.FloatField(verbose_name='平均价')
    priceMin = models.FloatField(verbose_name='最低价')

    productSize = models.CharField(max_length=128,verbose_name='规格')
    productPlace = models.CharField(max_length=128,verbose_name='产地')
    recordDate = models.DateField(verbose_name='发布日期')


    class Meta:
        verbose_name = '农产品管理'  # 定义在管理后台显示的名称
        verbose_name_plural = verbose_name  # 定义复数时的名称（去除复数的s）
        ordering = ['-recordDate']  # 排序





