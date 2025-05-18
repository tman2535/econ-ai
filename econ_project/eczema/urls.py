from django.urls import path
from . import views
app_name = 'eczema'
urlpatterns = [
    path('', views.upload_image, name='eczema_upload'),
    path('result/', views.cataract_result, name='eczema_result'),

]
