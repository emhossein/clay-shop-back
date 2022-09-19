# Generated by Django 4.1.1 on 2022-09-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_alter_items_id_alter_items_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsMens',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
                ('price', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
                ('color', models.CharField(max_length=200)),
                ('images', models.CharField(max_length=800)),
                ('category', models.CharField(max_length=200)),
                ('sub_category', models.CharField(max_length=200)),
                ('color_pic', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsWomens',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
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