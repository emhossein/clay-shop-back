from django.db import models


class Items(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    product_name = models.CharField(max_length=200)
    rating = models.FloatField()
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    color = models.CharField(max_length=200)
    images = models.CharField(max_length=800)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    color_pic = models.CharField(max_length=800)

    def __str__(self):
        return self.product_name


class ItemsMens(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    product_name = models.CharField(max_length=200)
    rating = models.FloatField()
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    color = models.CharField(max_length=200)
    images = models.CharField(max_length=800)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    color_pic = models.CharField(max_length=800)

    def __str__(self):
        return self.product_name


class ItemsWomens(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    product_name = models.CharField(max_length=200)
    rating = models.FloatField()
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    color = models.CharField(max_length=200)
    images = models.CharField(max_length=800)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    color_pic = models.CharField(max_length=800)

    def __str__(self):
        return self.product_name
