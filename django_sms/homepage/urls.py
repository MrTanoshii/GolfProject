from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomePageView
from django.urls import path
from .views import LoginView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup',views.signup,name='signup'),
    path('login/', LoginView.as_view(), name='login'),
   ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)