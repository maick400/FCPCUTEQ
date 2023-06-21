"""
URL configuration for FCPC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from FCPC import settings



urlpatterns = [
        path('Admin/', admin.site.urls),
    path('', include('core.urls'), name='core'),
    path('socios/', include('moduloSocios.urls'), name='socios'),
    path('creditos/', include('moduloCreditos.urls'), name='creditos'),
    path('contable/', include('moduloContable.urls'), name='contable'),
    path('fondo/', include('moduloFondo.urls'), name='fondo'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
