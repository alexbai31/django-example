"""phones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from main.views import view_people, export_to_excel, import_from_file

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view_people, name="main"),
    url(r'^page/(?P<page>[0-9]+)$', view_people, name="main"),
    url(r'^export/$', export_to_excel, name="export-landline"),
    url(r'^export/(?P<type>[a-z]+)', export_to_excel, name="export-landline"),
    url(r'^import/$', import_from_file, name="import")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

