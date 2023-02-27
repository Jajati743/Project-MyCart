from django.db import models

# Create your models here.
class product(models.Model):
    Product_id=models.AutoField
    Product_name=models.CharField(max_length=50)
    Category=models.CharField(max_length=50, default="")
    Subcategory=models.CharField(max_length=50, default="")
    Price=models.IntegerField(default=0)
    Desc=models.CharField(max_length=300)
    Pub_date=models.DateField()
    Image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.Product_name


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70, default="")
    phone=models.CharField(max_length=70, default="")
    desc=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    pin_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."