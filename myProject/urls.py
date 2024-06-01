"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from interfaceApp.views import homeview, contactview, aboutview
from paymentApp.views import paymentview
from shopApp.views import flagview, clothesview, utensilsview
from cartApp.views import clothes_cartview, flag_cartview, utensils_cartview
from userdata.views import signupview, loginview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview),
    path('', include('interfaceApp.urls')),
    path('', include('shopApp.urls')),
    path('', include('cartApp.urls')),
    path('', include('paymentApp.urls')),
    path('', include('userdata.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)