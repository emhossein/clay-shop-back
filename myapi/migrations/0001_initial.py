# Generated by Django 4.1.1 on 2022-09-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('price', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
                ('color', models.CharField(max_length=200)),
                ('images', models.CharField(max_length=800)),
                ('category', models.CharField(max_length=200)),
                ('sub_category', models.CharField(max_length=200)),
                ('color_pic', models.CharField(max_length=800)),
            ],
        ),
    ]