from django.urls import path
from . import views
app_name = 'dental_caries'
urlpatterns = [
    path('', views.upload_image, name='dental_caries_upload'),
    path('result/', views.cataract_result, name='dental_caries_result'),

]
