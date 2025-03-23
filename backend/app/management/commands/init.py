# coding=utf-8
"""
    @product  :   PyCharm
    @Author   :   xeon
    @date     :   2022/9/11 02:14
    @fileName :   init.py
    @功能      : 初始化
"""

from django.core.management.base import BaseCommand


def create_faker_info():
    from faker import Faker
    faker = Faker("zh-CN")
    # User.objects.all().delete()
    for i in range(100):
        # 生成指定时间的日期
        date = faker.date_between('-100day','today')
        simple_profile = faker.simple_profile()
        """
        {'username': 'songguiying',
         'name': '申凯',
         'sex': 'F',
         'address': '江苏省惠州县沈河官路f座 807064',
         'mail': 'yonggong@yahoo.com',
         'birthdate': datetime.date(1980, 6, 3)}
        """
        username = simple_profile['name']
        sex = '男' if simple_profile['sex']=='F' else '女'
        address = simple_profile['address']
        email = simple_profile['mail']
        birthdate = simple_profile['birthdate']
        tel  = faker.phone_number()
        # if not User.objects.filter(tel=tel):
        #     User.objects.create(time=time,email=email,username=username,password='123456',sex=sex,address=address,tel=tel)

class Command(BaseCommand):
    help = '初始化数据'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully closed poll!'))
        pass
        # try:
        #     poll = Poll.objects.get(pk=poll_id)
        # except Poll.DoesNotExist:
        #     raise CommandError('Poll "%s" does not exist' % poll_id)
        # self.stdout.write(self.style.SUCCESS('Successfully closed poll!'))