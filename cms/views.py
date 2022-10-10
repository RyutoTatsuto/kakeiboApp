from django.shortcuts import render
from django.http import HttpResponse

from cms.models import PurchaseHistories


def purchase_histories_list(request):
    """ 購入履歴の一覧を表示する """
    purchase_histories_list = (PurchaseHistories
                               .objects
                               .all()
                               .order_by('purchase_history_id'))
    
    return render(request,
                  'cms/',
                  {'purchase_histories_list': purchase_histories_list})