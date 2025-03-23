"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', TestView.as_view(),name='test'),  #  测试
    # ================================================= #
    # ****************** 数据入库和处理   ******************* #
    # ================================================= #
    path('sql2sql/', sql2sql, name='sql2sql'),  # 数据入库
    path('api/get_rice_list', get_rice_list,name='get_rice_list'),  #水稻列表
    path('api/get_products_list', get_products_list,name='get_products_list'),  #农产品列表
    path('api/get_rice_recommed', get_rice_recommed,name='get_rice_recommed'),  # 选择某省  选择分类属性（类型、母本、审定公司） 推荐排名前10 的水稻
    path('api/get_sheng_productList', get_sheng_productList,name='get_sheng_productList'),  # 获取某个省的 产品信息
    path('api/get_plot1', get_plot1,name='get_plot1'),  #  各省不同农产品的各种价格变化
    path('api/get_all_product', get_all_product,name='get_all_product'),  # 获取所有农产品信息
    path('api/get_plot2', get_plot2,name='get_plot2'),  # 不同农产品的价格对比
    path('api/get_plot3', get_plot3,name='get_plot3'),  # 各农产品产地数量饼图
    path('api/get_plot4', get_plot4,name='get_plot4'),  # 各省份蔬菜数量柱状图
    path('api/product_predict', product_predict,name='product_predict'),  # 使用机器学习算法预测各种农产品的价格趋势
    path('api/get_plot5', get_plot5,name='get_plot5'),  #分析近年农产品的价格随时间的变化，




    # ================================================= #
    # ****************** 待删除   ******************* #
    # ================================================= #
    path('api/login/', login,name='login'),  #  登录
    path('api/register/', register,name='register'),  #  注册
    path('api/user/info', user_info,name='user_info'),  # 获取用户信息
    path('api/user/update', user_update,name='user_update'),  # 更新用户信息
    path('api/user/password', user_password,name='user_password'),  # 更新用户密码

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 使用 rest_framework

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('test', TestView)