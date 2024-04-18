from django.urls import path
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from anxheloapp import views


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path('success/', views.contact_view, name='success'),
    path('i18n/set_language/', set_language, name='set_language'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)