
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

admin.site.site_header= "Farmestic Admin Panel"
admin.site.site_title = "Welcome To Farmestic"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/',include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns= urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)