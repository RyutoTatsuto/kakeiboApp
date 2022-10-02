from django.contrib import admin
from cms.models import PurchaseHistories, Residents, MajorCategories, PaymentMethods

''' DBのレコードの項目が詳細に見られるようにカスタマイズ '''


class ResidentsAdmin(admin.ModelAdmin):
    ''' 
    住民テーブル
    '''
    # adminに表示する項目
    list_display = ('resident_id', 'first_name', 'given_name',)
    # クリックできる項目
    list_display_links = ('resident_id',)


admin.site.register(Residents, ResidentsAdmin)
