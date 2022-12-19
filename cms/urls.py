from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    path('', views.purchase_histories_list, name='purchase_histories_list'),
    path('purchase_item/add/', views.purchase_item_edit, name='purchase_item_add'),
    path('purchase_item/edit/<int:purchase_history_id>', views.purchase_item_edit, name='purchase_item_edit'),
    path('purchase_item/delete/<int:purchase_history_id>', views.purchase_item_delete, name='purchase_item_delete'),
]