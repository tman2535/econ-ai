"""econ_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('cataract/', include('cataract.urls', namespace='cataract')),
    path('dryeye/', include('dryeye.urls', namespace='dryeye')),
    path('strabismus/', include('strabismus.urls', namespace='strabismus')),
    path('acne/', include('acne.urls', namespace='acne')),
    path('eczema/', include('eczema.urls', namespace='eczema')),
    path('psoriasis/', include('psoriasis.urls', namespace='psoriasis')),
    path('dental/', include('dental_caries.urls', namespace='dental_caries')),
    path('gingivitis/', include('gingivitis.urls', namespace='gingivitis')),
    path('', include('main.urls')),

]

# برای فایل‌های مدیا
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
