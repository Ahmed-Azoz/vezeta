# Generated by Django 3.1.1 on 2020-10-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201003_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(max_length=50, verbose_name='نبذه عنك'),
        ),
    ]