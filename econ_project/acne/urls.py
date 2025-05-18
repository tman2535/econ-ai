from django.urls import path
from . import views

app_name = 'acne'

urlpatterns = [
    path('', views.upload_image, name='acne_upload'),
    path('result/', views.cataract_result, name='acne_result'),

]
