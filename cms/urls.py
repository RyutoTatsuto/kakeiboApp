from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    path('', views.purchase_histories_list, name='purchase_histories_list'),
]