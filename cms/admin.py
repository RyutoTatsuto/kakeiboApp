from django.contrib import admin
from cms.models import PurchaseHistories, Residents, MajorCategories, PaymentMethods

''' DBのレコードの項目が詳細に見られるようにカスタマイズ '''


class MajorCategoriesAdmin(admin.ModelAdmin):
    '''
    大カテゴリテーブル
    '''
    # adminに表示する項目
    list_display = ('major_category_id', 'major_category_name',)
    # クリックできる項目
    list_display_links = ('major_category_id',)


class PaymentMethodsAdmin(admin.ModelAdmin):
    '''
    支払い方法テーブル
    '''
    # adminに表示する項目
    list_display = ('payment_method_id', 'payment_method_name',)
    # クリックできる項目
    list_display_links = ('payment_method_id',)


class ResidentsAdmin(admin.ModelAdmin):
    ''' 
    住民テーブル
    '''
    # adminに表示する項目
    list_display = ('resident_id', 'first_name', 'given_name',)
    # クリックできる項目
    list_display_links = ('resident_id',)


admin.site.register(Residents, ResidentsAdmin)
admin.site.register(MajorCategories, MajorCategoriesAdmin)
admin.site.register(PaymentMethods, PaymentMethodsAdmin)
