from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from cms.models import PurchaseHistories
from cms.forms import PurchaseItemForm


def purchase_histories_list(request):
    """ 購入履歴の一覧を表示する """
    purchase_histories_list = (PurchaseHistories
                               .objects
                               .all()
                               .order_by('purchase_history_id'))
    
    return render(request,
                  'cms/purchase_histories_list.html',
                  {'purchase_histories_list': purchase_histories_list})


def purchase_item_edit(request, purchase_history_id=None):
    ''' 購入したアイテムの登録・編集 '''
    if purchase_history_id is None:  # 購入したアイテムを追加
        purchase_item = PurchaseHistories()
    else:  # 購入したアイテムの情報を修正
        purchase_item = get_object_or_404(PurchaseHistories, pk=purchase_history_id)
    
    if request.method == 'POST':
        form = PurchaseItemForm(request.POST, instance=purchase_item)
        if form.is_valid():
            purchase_item = form.save(commit=False)
            purchase_item.save()
            return redirect('cms:purchase_histories_list')
    else:
        form = PurchaseItemForm(instance=purchase_item)

    return render(request, 'cms/purchase_item_edit.html', dict(form=form, purchase_history_id=purchase_history_id))


def purchase_item_delete(_, purchase_history_id):
    ''' 購入したアイテムの削除 '''
    purchase_item = get_object_or_404(PurchaseHistories, pk=purchase_history_id)
    purchase_item.delete()

    return redirect('cms:purchase_histories_list')
