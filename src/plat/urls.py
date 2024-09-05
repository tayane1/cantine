from django.urls import path
from .views import index, add_edit_plat, update_plat, delete_plat

app_name = 'plat'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_plat, name='add_plat'),
    path('update/<int:id>/', update_plat, name='update_plat'),
    path('delete/<int:id>/', delete_plat, name='delete_plat'),
]