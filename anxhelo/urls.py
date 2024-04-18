from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path('', include('anxheloapp.urls')),
    path(_('admin/'), admin.site.urls),
    prefix_default_language=False
)