from django.db import models
from . import managers

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stapmed Model """

    created = models.DateTimeField(auto_now_add=True)  # model 저장시 자동으로 날짜 기록
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True  # 데이터베이스에 등록 X
