
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('contact.urls')),
    path('',include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

# custome admin controle panale
admin.site.site_header = 'Welcome to Contact Project'
admin.site.site_title = 'Contact'
admin.site.index_title = 'Contact Project'
