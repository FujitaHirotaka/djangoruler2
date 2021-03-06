# Generated by Django 2.1.1 on 2018-10-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSpecie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie', models.CharField(max_length=255, unique=True, verbose_name='アプリ種')),
            ],
        ),
        migrations.CreateModel(
            name='DjangoProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, unique=True, verbose_name='プロジェクト名')),
                ('app0', models.CharField(max_length=255, verbose_name='アプリ0')),
                ('app1', models.CharField(max_length=255, verbose_name='アプリ1')),
                ('app2', models.CharField(max_length=255, verbose_name='アプリ2')),
                ('app3', models.CharField(max_length=255, verbose_name='アプリ3')),
                ('app4', models.CharField(max_length=255, verbose_name='アプリ4')),
                ('app5', models.CharField(max_length=255, verbose_name='アプリ5')),
                ('app6', models.CharField(max_length=255, verbose_name='アプリ6')),
                ('app7', models.CharField(max_length=255, verbose_name='アプリ7')),
                ('app8', models.CharField(max_length=255, verbose_name='アプリ8')),
                ('app9', models.CharField(max_length=255, verbose_name='アプリ9')),
            ],
        ),
    ]
