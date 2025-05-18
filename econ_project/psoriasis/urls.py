from django.urls import path
from . import views
app_name = 'psoriasis'
urlpatterns = [
    path('', views.upload_image, name='psoriasis_upload'),
    path('result/', views.cataract_result, name='psoriasis_result'),

]
