from django.urls import path
from . import views

app_name = 'dryeye'

urlpatterns = [
    path('', views.upload_image, name='dryeye_upload'),
    path('result/', views.cataract_result, name='dryeye_result'),

]
