from django.contrib import admin
from django.urls import include, path

# not for prod
# a slight hack
from django.conf import settings
from django.conf.urls.static import static

from core.views import index, contact


urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
