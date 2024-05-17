from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from aolswebapp import views

urlpatterns = [
    path('', views.home_page_view, name="index"),
    path('applynow/', views.apply_now, name="applynow"),
    path('contact_us_success/', views.contactussuccess, name="contact_us_success"),
    path('apply_now_success/', views.apply_now_success, name="apply_now_success"),
    path('i18n/set_language/', set_language, name='set_language'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)