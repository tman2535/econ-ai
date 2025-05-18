from django.urls import path
from . import views
app_name = 'gingivitis'
urlpatterns = [
    path('', views.upload_image, name='gingivitis_upload'),
    path('result/', views.cataract_result, name='gingivitis_result'),

]
