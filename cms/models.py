from email.policy import default
from django.db import models
from django.utils import timezone


class MajorCategories(models.Model):
    ''' 大カテゴリマスタ '''
    major_category_id = models.AutoField(primary_key=True)
    major_category_name = models.CharField('カテゴリ', max_length=20, blank=False, default='')

    def __str__(self) -> str:
        return self.major_category_name


class PaymentMethods(models.Model):
    ''' 支払い方法マスタ '''
    payment_method_id = models.AutoField(primary_key=True)
    payment_method_name = models.CharField('支払い方法', max_length=20, blank=False)

    def __str__(self) -> str:
        return self.payment_method_name


class Residents(models.Model):
    ''' 住民マスタ '''
    resident_id = models.AutoField(primary_key=True)
    first_name = models.CharField('姓', max_length=20, blank=False)
    given_name = models.CharField('名', max_length=20, blank=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.given_name}'


class PurchaseHistories(models.Model):
    ''' 購入履歴テーブル '''
    purchase_history_id = models.BigAutoField(primary_key=True)
    price = models.IntegerField('金額', default=0)
    major_category_id = models.ForeignKey(MajorCategories, on_delete=models.DO_NOTHING)
    payment_method_id = models.ForeignKey(PaymentMethods, on_delete=models.DO_NOTHING)
    payment_date = models.DateField('支払い日', default=timezone.now)
    resident_id = models.ForeignKey(Residents, on_delete=models.DO_NOTHING)
    memo = models.TextField('メモ', blank=True, default="")
    editing_time = models.DateTimeField('修正日時', default=timezone.now)
    registering_time = models.DateTimeField('登録時間', default=timezone.now)

    def __str__(self) -> str:
        return str(self.purchase_history_id)
