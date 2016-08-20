from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
    
    url(r'^app001/', include('app001.urls')),
    #
    url(r'^admin/', admin.site.urls),
    
    # http://tutorial.djangogirls.org/en/django_models/
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    # url(r'', include('blog.urls')),
]
