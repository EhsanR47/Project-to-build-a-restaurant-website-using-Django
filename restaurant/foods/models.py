from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import gettext as _
# Create your models here.
class Food(models.Model):
    FOOD_TYPE=[
        ("breakfast","صبحانه"),
        ("drinks","نوشیدنی"),
        ("dinner","شام"),
        ("lunch","ناهار")
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(_("توضیحات"), max_length=50)
    rate = models.IntegerField("امتیاز",default=0)
    price = models.IntegerField()
    time = models.IntegerField("زمان لازم")
    pub_date = models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to="foods/")
    type_food = models.CharField(_("نوع غذا"), max_length=10,choices=FOOD_TYPE,default="drinks")
    def __str__(self):
        return self.name