from django.contrib.auth import get_user_model
from django.db import models


class ProductAndService(models.Model):
    class  Business(models.IntegerChoices):
        PRODUCT = 0, 'Товар'
        SERVICE = 1, 'Услуга'

    offer = models.BooleanField(choices=Business.choices, default=Business.PRODUCT)
    name = models.CharField(max_length=100, verbose_name='Кратко расскажите про товар/услугу')
    description = models.CharField(max_length=2000, verbose_name='Расскажите развернуто про товар/услугу')
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product_and_service')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.name