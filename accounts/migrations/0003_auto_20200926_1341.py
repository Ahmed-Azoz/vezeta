# Generated by Django 3.1.1 on 2020-09-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200926_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(verbose_name='سعر الكشف'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='who_i',
            field=models.TextField(max_length=250, verbose_name='من انا'),
        ),
    ]