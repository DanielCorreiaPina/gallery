from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:image_id>/', views.details, name='details'),
    path('', views.upload, name='upload'),
]