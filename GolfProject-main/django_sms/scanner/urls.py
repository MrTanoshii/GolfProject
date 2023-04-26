from django.urls import path
from .views import ScannerView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('scanner/', ScannerView.as_view(), name='scanner'),
    # other URL patterns...
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)