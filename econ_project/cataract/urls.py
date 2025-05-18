from django.urls import path
from . import views

app_name = 'cataract'

urlpatterns = [
    path('', views.upload_image, name='cataract_upload'),
    path('result/', views.cataract_result, name='cataract_result'),

]
