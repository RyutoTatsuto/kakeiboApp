from dataclasses import fields
from django.forms import ModelForm
from cms.models import PurchaseHistories


class PurchaseItemForm(ModelForm):
    ''' 購入したアイテムの登録・修正用のフォーム '''
    class Meta:
        model = PurchaseHistories
        fields = ('payment_date', 'price',
                  'major_category_id', 'payment_method_id', 'resident_id', 'memo')
