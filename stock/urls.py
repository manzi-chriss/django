from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stock/', views.stock, name='stock'),
    path('retrieve/',views.view , name='retrieve') ,
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('list', views.item_list,name='list'),
    path('update/<int:pk>/', views.update_item, name='update_item'),
     path('add/', views.add_item, name='add_item'),
     

]
