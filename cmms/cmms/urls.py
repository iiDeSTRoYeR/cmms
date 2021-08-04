import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
    path('tasks/', include('tasks.urls')),
    path('consumable/', include('consumable.urls')),
    path('employees/', include('employees.urls')),
    path('inventory/', include('inventory.urls')),
    path('spareparts/', include('spareparts.urls')),
    path('supplier/', include('supplier.urls')),
    path('usage/', include('usage.urls')),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
#Test by Ahmed v1
#Test by Ahmed v2
