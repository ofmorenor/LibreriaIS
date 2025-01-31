"""libreriaIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path, include
from django.views.generic.base import TemplateView

from core.views import home, detalleslug,SignUpView, detalleslug, BootstrapFilterView

urlpatterns = [
    path('', home, name='home'),
    path('libro/<slug:slug>/', detalleslug, name='libro'),
    path('busqueda/', BootstrapFilterView, name='busqueda'),
    #path('busqueda/', Detallesbusqueda.as_view(), name='busqueda'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

