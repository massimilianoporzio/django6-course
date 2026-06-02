from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item_generic'),
    path('item/<int:item_id>/', views.item, name='item'),
]