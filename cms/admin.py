from django.contrib import admin
from cms.models import PurchaseHistories, Residents, MajorCategories, PaymentMethods

admin.site.register(PurchaseHistories)
admin.site.register(Residents)
admin.site.register(MajorCategories)
admin.site.register(PaymentMethods)