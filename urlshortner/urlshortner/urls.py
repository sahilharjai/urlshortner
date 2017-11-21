"""urlshortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,static
from django.contrib import admin
import shortner.views_api as views_api
import shortner.views as views   
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/url-create/$', views_api.URLCreateView.as_view(),name='url-create'),
    url(r'^$',views.URLHomeView.as_view(),name='home'),
    url(r'^analyse/(?P<shortcode>[\w-]+)/$',views.URLAnalyseView.as_view(),name='analyse'),
    url(r'^(?P<shortcode>[\w-]+)/$', views_api.URLRedirectView.as_view(), name='scode'), 
]+ static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
