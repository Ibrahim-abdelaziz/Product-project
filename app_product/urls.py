from django.urls import path, include
from .views import all_product,one_product,add_product,add,new_form



urlpatterns = [
    path('all_product',all_product,name='all_product'),
    path('one_product/<str:name>/', one_product,name='one_product'),
    path('add_product', add_product, name='add_product'),
    path('add', add, name='add'),
    path('new_form',new_form,name='new_form'),

]
