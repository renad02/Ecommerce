from django.db import models

# Create your models here.

class storetype(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class items(models.Model):                                        # مرتبط مع Storetype
    nameitems=models.CharField(max_length=50)                         #اسم النتج 
    description=models.CharField(max_length=200)                    # وصف المنتج
    image=models.ImageField(upload_to='images/',null=True)            # صورة المنتج
    price=models.FloatField()                                      # سعر المنتج
    availability=models.BooleanField()                              # اذا كان المنتج متوفر او لا ,هنا النوع بولين 
    st=models.ForeignKey(storetype,on_delete=models.CASCADE,null=True)            # ربط المنتج ب التصنيف او القسم زي التيشرت من قسم الملابس
    def __str__(self):
        template='{0.nameitems} {0.description} {0.image} {0.price} {0.availability}'
        return template.format(self)

class itemsdetails(models.Model):                       # items مرتبط مع  
    color=models.CharField(max_length=50)               # الجدول هذا عباره هن بيانات زياده للمنتج 
    qty=models.FloatField()
    tax=models.FloatField()
    barcode=models.CharField(max_length=200)                          # الارقام الطويله اللي تجي للمنتج 
    country=models.CharField(max_length=50)                             # بلد الصنع     
    items=models.ForeignKey(items,on_delete=models.CASCADE,null=True)
    def __str__(self):
        template='{0.color} {0.qty} {0.tax} {0.barcode} {0.country}'
        return template.format(self)
    

class cart(models.Model):                       # هاذي عشان السله , والسله هي جدول الفاتوره المؤقت
    itmesid=models.IntegerField()               #  يضيف رقم المنتج في السله ورقم المستخدم