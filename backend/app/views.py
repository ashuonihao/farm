# 导入库
import warnings

import pandas as pd
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
warnings.filterwarnings("ignore")
#  可视化
# 机器学习
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

warnings.filterwarnings('ignore')
from app.models import *
# import logging
# # 日志输出常量定义
# logger = logging.getLogger('mylogger')
# logger.info("post request body 请求数据提交")


def init_user():
    # 初始化普通用户
    from app import models
    if not models.User.objects.filter(tel="user", password="123456"):
        models.User.objects.create(tel="user", password="123456", username="user")

    # 初始化管理员
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin'):
        User.objects.create_superuser('admin', 'admin@qq.com', 'admin')


# 第一步输入这个：去除开头警告
import warnings

warnings.simplefilter('ignore', ResourceWarning)
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
import os
import datetime
import json
import warnings
from tqdm import tqdm

warnings.filterwarnings('ignore')


class TestView(View):
    # 查
    def get(self, request):
        print(request.headers['Authorization'])

        return JsonResponse({'status': 200, 'msg': '操作成功'})

    # 增加
    def post(self, request):
        return HttpResponse('post方法')
        return JsonResponse({'status': 200, 'msg': '操作成功'})

    # 修改
    def put(self, request):
        return HttpResponse('post方法')
        return JsonResponse({'status': 200, 'msg': '操作成功'})

    # 删除
    def delete(self, request):
        return HttpResponse('post方法')
        return JsonResponse({'status': 200, 'msg': '操作成功'})


class TmpView(View):
    # 查
    def get(self, request):
        user = request.headers['Authorization']
        uid = json.loads(user)["id"]
        pk = request.GET.get("id")
        return render(request, '.html', locals())

    # 增加
    def post(self, request):
        user = request.headers['Authorization']
        uid = json.loads(user)["id"]
        postBody = request.body  # 实质上是个字符串
        json_result = json.loads(postBody)  # json库处理后变为字典格式，内部有嵌套层级
        print(json_result)
        return HttpResponse('post方法')
        return JsonResponse({'status': 200, 'msg': '操作成功'})

    # 修改
    def put(self, request):
        return HttpResponse('post方法')
        return JsonResponse({'status': 200, 'msg': '操作成功'})

    # 删除

def delete(self, request):

    def delete(self, request):

        return HttpResponse('post方法')
        return JsonResponse({'status': 200, 'msg': '操作成功'})


def login(request):
    postBody = request.body  # 实质上是个字符串
    json_result = json.loads(postBody)  # json库处理后变为字典格式，内部有嵌套层级
    print(json_result)
    if User.objects.filter(username=json_result["username"], password=json_result["password"]):
        data = User.objects.filter(username=json_result["username"], password=json_result["password"]).values()[0]
        return JsonResponse({'code': 200, 'msg': '操作成功', "data": data})
    else:
        return JsonResponse({'code': 201, 'msg': '失败'})


def register(request):
    postBody = request.body  # 实质上是个字符串
    json_result = json.loads(postBody)  # json库处理后变为字典格式，内部有嵌套层级
    print(json_result)
    if User.objects.filter(username=json_result["username"]):
        return JsonResponse({'code': 201, 'msg': '该用户名已被注册，请修改！'})
    else:
        User.objects.create(**json_result)
        return JsonResponse({'code': 200, 'msg': '操作成功'})


def user_info(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    print(uid)
    data = User.objects.filter(id=uid).values()[0]
    return JsonResponse({'code': 200, 'msg': '操作成功', "data": data})


def user_update(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    print(uid)
    postBody = request.body  # 实质上是个字符串
    json_result = json.loads(postBody)  # json库处理后变为字典格式，内部有嵌套层级
    User.objects.filter(id=uid).update(**json_result)
    data = User.objects.filter(id=uid).values()[0]
    return JsonResponse({'code': 200, 'msg': '操作成功', "data": data})


def user_password(request):
    print("geng")
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    print(uid)
    postBody = request.body  # 实质上是个字符串
    json_result = json.loads(postBody)  # json库处理后变为字典格式，内部有嵌套层级

    if User.objects.filter(id=uid, password=json_result["oldpassword"]):
        User.objects.filter(id=uid, password=json_result["oldpassword"]).update(password=json_result["password"])
        return JsonResponse({'code': 200, 'msg': '操作成功'})
    else:
        return JsonResponse({'code': 201, 'msg': '操作成功'})


# mysql数据库数据存到数据库  完成一定的数据清洗
def sql2sql(request):
    # 1 水稻入库
    # 加载的文件名
    filename = os.path.join("data", "水稻数据_清洗.csv")
    # 数据
    raw_data = pd.read_csv(filename)
    # 去重
    print(f"去重前的长度{len(raw_data)}")
    raw_data = raw_data.drop_duplicates()
    print(f"去重后的长度{len(raw_data)}")
    # ['省份', '品种名称', '亲本来源', '类型', '原产地', '审定编号', '审定方',
    # '审定序号', '母本', '审定公司']

    print(raw_data.columns)
    for i in tqdm(range(len(raw_data))):
        sheng = raw_data.iloc[i]["省份"]
        pzlx = raw_data.iloc[i]["品种名称"]
        qbly = raw_data.iloc[i]["亲本来源"]
        lx = raw_data.iloc[i]["类型"]
        ycd = raw_data.iloc[i]["原产地"]
        sdbh = raw_data.iloc[i]["审定编号"]
        sdf = raw_data.iloc[i]["审定方"]
        sdxh = raw_data.iloc[i]["审定序号"]
        mb = raw_data.iloc[i]["母本"]
        sdgs = raw_data.iloc[i]["审定公司"]
        data = {
            'sheng': sheng,
            'pzlx': pzlx,
            'qbly': qbly,
            'lx': lx,
            'ycd': ycd,
            'sdbh': sdbh,
            'sdf': sdf,
            'sdxh': sdxh,
            'mb': mb,
            'sdgs': sdgs,
            'recordDate': '2024-02-27'

        }
        # 如果不存在数据，新增
        if not Rice.objects.filter(**data):
            Rice.objects.create(**data)
    # 2 农产品
    # 加载的文件名
    filename = os.path.join("data", "农产品数据_清洗.csv")
    # 数据
    raw_data = pd.read_csv(filename)
    # 去重
    print(f"去重前的长度{len(raw_data)}")
    raw_data = raw_data.drop_duplicates()
    print(f"去重后的长度{len(raw_data)}")
    #
    # 分类 品名 最高价 平均价  最低价 单位 规格 产地 发布日期
    columns = ['categoryName', 'productName', 'priceMax', 'priceAvg', 'priceMin',
               'unit', 'productSize', 'productPlace', 'recordDate', ]

    print(raw_data.columns)
    for i in tqdm(range(len(raw_data))):
        data = raw_data.iloc[i]
        data = dict(data)
        # 如果不存在数据，新增
        # 如果不存在数据，新增
        if not Products.objects.filter(**data):
            Products.objects.create(**data)

    return HttpResponse('ok')


def get_rice_list(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    name = request.GET.get('name')
    kind = request.GET.get('kind')
    pageSize = request.GET.get('pageSize')
    pagenum = request.GET.get('pagenum')
    pageSize, pagenum = int(pageSize), int(pagenum)

    # 原始数据获取
    data_list = Rice.objects.all()
    # 类别
    kind_list = sorted(set([i.sheng for i in data_list]))
    kind_list = list(kind_list)

    # 数据过滤
    data_list = data_list.filter(pzlx__contains=name, sheng__contains=kind)
    data_list = data_list.values()

    # 总数
    total = len(data_list)
    # 开始
    begin = (pagenum - 1) * pageSize
    # 结束
    end = (pagenum - 0) * pageSize
    # 分页
    data_list = data_list[begin:end]
    print(begin, end)

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "data_list": data_list, 'kind_list': kind_list, 'total': total
                         })


from django.http import JsonResponse
from app.models import Products
import logging

logger = logging.getLogger(__name__)

def get_products_list(request):
    try:
        # 获取uid
        uid = request.headers.get('Authorization')
        if uid is None:
            return JsonResponse({'code': 401, 'msg': '未提供用户 ID'}, status=401)
        uid = int(uid)

        # 获取get数据
        print(request.GET)
        name = request.GET.get('name', '')
        kind = request.GET.get('kind', '')
        pageSize = request.GET.get('pageSize', '10')
        pagenum = request.GET.get('pagenum', '1')

        try:
            pageSize = int(pageSize)
            pagenum = int(pagenum)
        except ValueError:
            return JsonResponse({'code': 400, 'msg': '页码或每页数量必须为整数'}, status=400)

        # 原始数据获取
        data_list = Products.objects.all()

        # 类别
        kind_list = sorted(set([i.productPlace for i in data_list]))
        # '' 表示 不搞条件了
        kind_list = ['', ] + list(kind_list)

        # 数据过滤
        data_list = data_list.filter(productName__contains=name, productPlace__contains=kind)

        # 总数
        total = data_list.count()

        # 开始
        begin = (pagenum - 1) * pageSize
        # 结束
        end = pagenum * pageSize

        # 分页
        data_list = data_list[begin:end].values()

        print(begin, end)

        return JsonResponse({'code': 200, 'msg': '操作成功',
                             "data_list": list(data_list), 'kind_list': kind_list, 'total': total
                             })
    except Exception as e:
        logger.error(f"获取产品列表时出现错误: {e}")
        return JsonResponse({'code': 500, 'msg': '服务器内部错误'}, status=500)


def get_rice_recommed(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    type = request.GET.get('type')
    kind = request.GET.get('kind')

    raw_data = Rice.objects.filter(sheng=kind)
    # 类别
    kind_list = sorted(set([i.sheng for i in raw_data]))

    type2name = {
        '类型': 'lx',
        '母本': 'mb',
        '审定公司': 'sdgs',
    }
    tmp_data = raw_data.values(type2name[type]).annotate(count=Count(type2name[type]))
    # 排序
    tmp_data = sorted(tmp_data, key=lambda x: x['count'], reverse=True)[:10]
    x_data = [i[type2name[type]] for i in tmp_data]
    y_data = [i['count'] for i in tmp_data]
    print(tmp_data)

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "kind_list": kind_list,
                         "x_data": x_data,
                         "y_data": y_data,
                         })


def get_sheng_productList(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    kind = request.GET.get('kind')

    raw_data = Products.objects.filter(productPlace__contains=kind)
    data_list = list(set([i.productName for i in raw_data]))

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "data_list": data_list,
                         })


def get_plot1(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    kind = request.GET.get('kind')
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')

    raw_data = Products.objects.filter(productPlace__contains=kind)
    legend = [p1, p2]
    x_data = sorted(list(set([i.recordDate for i in raw_data])))
    x_data = [datetime.datetime.strftime(i, '%Y-%m-%d') for i in x_data]

    # 最高价格
    series1 = []
    for legen in legend:
        one = {
            'name': legen,
            'data': [],
            'type': 'line'
        }
        data = []
        for date in x_data:
            tmp = raw_data.filter(productName=legen, recordDate=date)
            data.append(None if tmp.count() == 0 else tmp[0].priceMax)
        one['data'] = data
        series1.append(one)
    # 最低价格
    series2 = []
    for legen in legend:
        one = {
            'name': legen,
            'data': [],
            'type': 'line'
        }
        data = []
        for date in x_data:
            tmp = raw_data.filter(productName=legen, recordDate=date)
            data.append(None if tmp.count() == 0 else tmp[0].priceMin)
        one['data'] = data
        series2.append(one)
    # 平均价格
    series3 = []
    for legen in legend:
        one = {
            'name': legen,
            'data': [],
            'type': 'line'
        }
        data = []
        for date in x_data:
            tmp = raw_data.filter(productName=legen, recordDate=date)
            data.append(None if tmp.count() == 0 else tmp[0].priceAvg)
        one['data'] = data
        series3.append(one)

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "x_data": x_data,
                         "legend": legend,
                         "series1": series1,
                         "series2": series2,
                         "series3": series3,
                         })


def get_all_product(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据

    raw_data = Products.objects.all()
    data_list = list(set([i.productName for i in raw_data]))

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "data_list": data_list,
                         })


def get_plot2(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')

    raw_data = Products.objects.all()
    legend = [p1, p2]
    x_data = sorted(list(set([i.recordDate for i in raw_data])))
    x_data = [datetime.datetime.strftime(i, '%Y-%m-%d') for i in x_data]

    # 最高价格
    series1 = []
    for legen in legend:
        one = {
            'name': legen,
            'data': [],
            'type': 'line'
        }
        data = []
        for date in x_data:
            tmp = raw_data.filter(productName=legen, recordDate=date)
            data.append(None if tmp.count() == 0 else tmp[0].priceMax)
        one['data'] = data
        series1.append(one)
    # 最低价格
    series2 = []
    for legen in legend:
        one = {
            'name': legen,
            'data': [],
            'type': 'line'
        }
        data = []
        for date in x_data:
            tmp = raw_data.filter(productName=legen, recordDate=date)
            data.append(None if tmp.count() == 0 else tmp[0].priceMin)
        one['data'] = data
        series2.append(one)
    # 平均价格
    series3 = []
    for legen in legend:
        one = {
            'name': legen,
            'data': [],
            'type': 'line'
        }
        data = []
        for date in x_data:
            tmp = raw_data.filter(productName=legen, recordDate=date)
            data.append(None if tmp.count() == 0 else tmp[0].priceAvg)
        one['data'] = data
        series3.append(one)

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "x_data": x_data,
                         "legend": legend,
                         "series1": series1,
                         "series2": series2,
                         "series3": series3,
                         })


def get_plot3(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    p1 = request.GET.get('p1')

    pro_list = ['广东', '广西', '河南', '海南', '湖北', '湖南']

    raw_data = Products.objects.filter(productName=p1)
    data = []
    for pro in pro_list:
        leng = raw_data.filter(productPlace__contains=pro).count()
        data.append({'value': leng, 'name': pro})

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "data": data,
                         })


def get_plot4(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    kind = request.GET.get('kind')

    pro_list = ['广东', '广西', '河南', '海南', '湖北', '湖南']

    raw_data = Products.objects.filter(productPlace__contains=kind, categoryName='蔬菜类')

    data_dict = {}
    for i in raw_data:
        data_dict.setdefault(i.productName, 0)
        data_dict[i.productName] += 1

    data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
    x_data = [i[0] for i in data]
    y_data = [i[1] for i in data]

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "x_data": x_data,
                         "y_data": y_data,
                         })


# 获取过去多少天的日期列表
def get_future_date(end_time_str='2024-02-27', days=7, is_str=True):
    """
    获取过去多少天的日期列表
    end_time_str 起止时间
    days 过去多少天
    is_str 是否字符串
    get_future_date(end_time_str='2024-02-27',days=180,is_str=True)
    """
    import datetime
    this_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d')  # 日期对象
    data = []
    for i in range(1, days + 1):
        tmp_time = this_time + datetime.timedelta(days=i)
        data.append(tmp_time)
    # 转换字符串
    if is_str:
        data = [datetime.datetime.strftime(i, '%Y-%m-%d') for i in data]  # 日期字符串
    print(data)
    return data


def product_predict(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    p1 = request.GET.get('p1')
    kind = request.GET.get('kind')

    # 预测未来一周数据构建
    days = 7
    future_data_str = get_future_date(end_time_str='2024-02-27', days=days, is_str=True)
    future_data = get_future_date(end_time_str='2024-02-27', days=days, is_str=False)
    pre_data = [
        [i.year, i.month, i.day]
        for i in future_data
    ]

    # 获取数据集
    raw_data = Products.objects.filter(productName=p1, productPlace__contains=kind).values()
    # # 数据集特征  年 月 日
    columns = ['recordDate', 'priceMax', 'priceAvg', 'priceMin', ]
    raw_df = pd.DataFrame(raw_data)
    raw_df = raw_df[columns]
    raw_df['year'] = raw_df['recordDate'].apply(lambda x: x.year)
    raw_df['month'] = raw_df['recordDate'].apply(lambda x: x.month)
    raw_df['day'] = raw_df['recordDate'].apply(lambda x: x.day)

    # 1 最高价格
    columns = ['year', 'month', 'day', ]
    x_train = raw_df[columns]
    y_train = raw_df['priceMax']
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, shuffle=True)

    # 构建模型
    # 1 用交叉验证法选择 随机森林回归 'n_estimators'最优的参数
    import time
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import GridSearchCV  # 网格搜索
    rf = RandomForestRegressor(random_state=10)
    time1 = time.time()
    param_1 = {'n_estimators': list(range(400, 1000, 100))}
    model_1 = GridSearchCV(estimator=rf, param_grid=param_1, cv=5, n_jobs=-1)
    model_1.fit(x_train, y_train)
    print("model1 最好的分数：{}".format(model_1.best_score_))
    print("model1 测试集的分数:{}".format(model_1.score(x_test, y_test)))
    print("model1 最好的参数：{}".format(model_1.best_params_))
    print("model1 消耗时间time=", time.time() - time1)  # 时间大概十分钟

    # 预测
    pre_list = model_1.predict(pre_data)
    pre_data1 = [round(i, 1) for i in pre_list]

    # 2 最低价格
    columns = ['year', 'month', 'day', ]
    x_train = raw_df[columns]
    y_train = raw_df['priceMin']
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, shuffle=True)

    # 构建模型
    # 1 用交叉验证法选择 随机森林回归 'n_estimators'最优的参数
    import time
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import GridSearchCV  # 网格搜索
    rf = RandomForestRegressor(random_state=10)
    time1 = time.time()
    param_1 = {'n_estimators': list(range(400, 1000, 100))}
    model_1 = GridSearchCV(estimator=rf, param_grid=param_1, cv=5, n_jobs=-1)
    model_1.fit(x_train, y_train)
    print("model1 最好的分数：{}".format(model_1.best_score_))
    print("model1 测试集的分数:{}".format(model_1.score(x_test, y_test)))
    print("model1 最好的参数：{}".format(model_1.best_params_))
    print("model1 消耗时间time=", time.time() - time1)  # 时间大概十分钟

    # 预测
    pre_list = model_1.predict(pre_data)
    pre_data2 = [round(i, 1) for i in pre_list]

    # 3 平均价格
    columns = ['year', 'month', 'day', ]
    x_train = raw_df[columns]
    y_train = raw_df['priceAvg']
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, shuffle=True)

    # 构建模型
    # 1 用交叉验证法选择 随机森林回归 'n_estimators'最优的参数
    import time
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import GridSearchCV  # 网格搜索
    rf = RandomForestRegressor(random_state=10)
    time1 = time.time()
    param_1 = {'n_estimators': list(range(400, 1000, 100))}
    model_1 = GridSearchCV(estimator=rf, param_grid=param_1, cv=5, n_jobs=-1)
    model_1.fit(x_train, y_train)
    print("model1 最好的分数：{}".format(model_1.best_score_))
    print("model1 测试集的分数:{}".format(model_1.score(x_test, y_test)))
    print("model1 最好的参数：{}".format(model_1.best_params_))
    print("model1 消耗时间time=", time.time() - time1)  # 时间大概十分钟

    # 预测
    pre_list = model_1.predict(pre_data)
    pre_data3 = [round(i, 1) for i in pre_list]

    x_data = future_data_str
    legend = ['最高价格', '最低价格', '平均价格']

    series = [
        {
            'name': '最高价格',
            'data': pre_data1,
            'type': 'line'
        },
        {
            'name': '最低价格',
            'data': pre_data2,
            'type': 'line'
        },
        {
            'name': '平均价格',
            'data': pre_data3,
            'type': 'line'
        },
    ]

    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "x_data": x_data,
                         "legend": legend,
                         "series": series,
                         })


def get_plot5(request):
    # 获取uid
    uid = request.headers['Authorization']
    uid = int(uid)
    # 获取get数据
    print(request.GET)
    p1 = request.GET.get('p1')
    kind = request.GET.get('kind')

    # 获取数据集
    raw_data = Products.objects.filter(productName=p1, productPlace__contains=kind)

    x_data_date = sorted(list(set([i.recordDate for i in raw_data])))
    x_data = [datetime.datetime.strftime(i, '%Y-%m-%d') for i in x_data_date]
    legend = ['最高价格', '最低价格', '平均价格']

    # 最高价格
    data1 = []
    for date in x_data:
        t = raw_data.filter(recordDate=date)[0].priceMax
        data1.append(t)
    # 最低价格
    data2 = []
    for date in x_data:
        t = raw_data.filter(recordDate=date)[0].priceMin
        data2.append(t)
    # 平均价格
    data3 = []
    for date in x_data:
        t = raw_data.filter(recordDate=date)[0].priceAvg
        data3.append(t)
    series = [
        {
            'name': '最高价格',
            'data': data1,
            'type': 'line'
        },
        {
            'name': '最低价格',
            'data': data2,
            'type': 'line'
        },
        {
            'name': '平均价格',
            'data': data3,
            'type': 'line'
        },
    ]
    return JsonResponse({'code': 200, 'msg': '操作成功',
                         "x_data": x_data,
                         "legend": legend,
                         "series": series,
                         })
