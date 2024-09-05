from django.urls import path
from .views import index, add_menu, update_menu, delete_menu

app_name = 'menu'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_menu, name='add_menu'),
    path('update/<int:id>/', update_menu, name='update_menu'),
    path('delete/<int:id>/', delete_menu, name='delete_menu'),
]