# Register your models here.
from django.contrib import admin
from app.models import *

# admin.py
admin.site.site_header = '农产品预测管理系统'  # 登录显示
admin.site.site_title = '农产品预测管理系统'  # title
admin.site.index_title = '农产品预测管理系统'  #

@admin.register(User)
#admin.site.register(User,  UserAdmin)
class UserAdmin(admin.ModelAdmin):
    # list_display用于设置列表页面要显示的不同字段
    list_display = ['id', 'tel', 'password', 'username', 'sex', 'address',

                    ]
    # search_fields用于设置搜索栏中要搜索的不同字段
    search_fields = ['username']

@admin.register(Rice)
#admin.site.register(User,  UserAdmin)
class RiceAdmin(admin.ModelAdmin):
    # list_display用于设置列表页面要显示的不同字段
    list_display = ['id', 'sheng', 'pzlx', 'qbly', 'lx', 'ycd',
                    'sdbh', 'sdf', 'sdxh', 'mb', 'sdgs', 'recordDate',

                    ]
    # search_fields用于设置搜索栏中要搜索的不同字段
    search_fields = [ 'sheng', 'pzlx', 'qbly', 'lx', 'ycd',
                    'sdbh', 'sdf', 'sdxh', 'mb', 'sdgs', 'recordDate',

                    ]

@admin.register(Products)
#admin.site.register(User,  UserAdmin)
class ProductsAdmin(admin.ModelAdmin):
    # list_display用于设置列表页面要显示的不同字段
    list_display = ['id','categoryName', 'productName', 'priceMax', 'priceAvg', 'priceMin',
               'unit', 'productSize', 'productPlace', 'recordDate', ]
    # search_fields用于设置搜索栏中要搜索的不同字段
    search_fields = ['categoryName', 'productName', 'priceMax', 'priceAvg', 'priceMin',
               'unit', 'productSize', 'productPlace', 'recordDate', ]