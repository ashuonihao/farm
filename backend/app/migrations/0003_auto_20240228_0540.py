# Generated by Django 2.2.4 on 2024-02-27 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20240228_0531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-recordDate'], 'verbose_name': '农产品管理', 'verbose_name_plural': '农产品管理'},
        ),
        migrations.AlterModelOptions(
            name='rice',
            options={'ordering': ['-recordDate'], 'verbose_name': '水稻管理', 'verbose_name_plural': '水稻管理'},
        ),
    ]
