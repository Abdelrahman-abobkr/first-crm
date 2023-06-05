from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('create/<int:id>/', views.create, name='create'),
    path('<str:slug>/', views.customer, name='customer'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
