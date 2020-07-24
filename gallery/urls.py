from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:image_id>/', views.details, name='details'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:image_id>/', views.delete_item, name='delete_item')
]