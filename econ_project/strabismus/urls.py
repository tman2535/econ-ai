from django.urls import path
from . import views
app_name = 'strabismus'
urlpatterns = [
    path('', views.upload_image, name='strabismus_upload'),
    path('result/', views.cataract_result, name='strabismus_result'),

]
