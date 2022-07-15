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
    path('update_voucher',views.update_voucher,name='update_voucher'),
    path('stockgrpscreate',views.stockgrpscreate,name='stockgrpscreate'),
    path('stockgrpcreate',views.stockgrpcreate,name='stockgrpcreate'),

    path('godwn',views.godwn,name='godwn'),
    path('godwn_alter',views.godwn_alter,name='godwn_alter'),
    path('stock_grp',views.stock_grp,name='stock_grp'),
    path('stock_cat',views.stock_cat,name='stock_cat'),
    path('stock_items',views.stock_items,name='stock_items'),


    path('stockgrp',views.stockgrp,name='stockgrp'),
    path('stockcate',views.stockcate,name='stockcate'),
    path('add_stockgrp',views.add_stockgrp,name='add_stockgrp'),
    path('add_stockcate',views.add_stockcate,name='add_stockcate'),
    path('stock_items',views.stock_items,name='stock_items'),
    path('add_stockitem',views.add_stockitem,name='add_stockitem'),

    path('stunits',views.stunits,name='stunits'),
    path('add_units',views.add_units,name='add_units'),

]