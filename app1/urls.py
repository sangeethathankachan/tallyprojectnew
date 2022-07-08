from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('changecompony',views.changecompony,name='changecompony'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('group',views.group,name='group'),
    path('crtcompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),
    path('create_group',views.create_group,name='create_group'),
    path('groups',views.groups,name='groups'),
    path('editgroup',views.editgroup,name='editgroup'),
    path('currency',views.currency,name='currency'),
    path('currencycreate',views.currencycreate,name='currencycreate'),
    path('voucher',views.voucher,name='voucher'),
    path('createvoucher',views.createvoucher,name='createvoucher'),
    path('save_ledger',views.save_ledger,name='save_ledger'),
    path('create_voucher',views.create_voucher,name='create_voucher'),
    path('currency_alter',views.currency_alter,name='currency_alter'),
    path('update_currency/<int:pk>',views.update_currency,name='update_currency'),
    path('godown',views.godown,name='godown'),
    path('stockcategory',views.stockcategory,name='stockcategory'),
    path('stockgroup',views.stockgroup,name='stockgroup'),
    path('stockitem',views.stockitem,name='stockitem'),
    path('unit',views.unit,name='unit'),

]