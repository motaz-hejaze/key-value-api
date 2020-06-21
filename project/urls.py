"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Key-Value Records Rest API",
      default_version='v1',
      description=
        """
            <h3>I used both functional approach and class based approach
            While the api is visually documented on /
            I recommend using Tools like Postman for testing</h3>
            <hr>
            <h3>URL LIST:</h3>
                GET <a href="/api/v1/keys">/api/v1/keys/</a><br>
                GET <a href="/api/v1/keys?filter=">/api/v1/keys?filter=</a> ==> with ?filter={} query parameter<br>
                PUT <a href="/api/v1/keys">/api/v1/keys</a> ==> with json {"key":"" , "value":""} <br>
                PUT <a href="/api/v1/keys?expire_in=">/api/v1/keys?expire_in=</a> ==> with json {"key":"" , "value":""} + ?expire_in={} query parameter<br>
                DELETE <a href="/api/v1/keys">/api/v1/keys</a><br>
                --------------------------<br>
                GET <a href="/api/v1/key/{id}">/api/v1/key/{id}</a>  ==> replace {id} with integer id <br>
                HEAD <a href="/api/v1/key/{id}">/api/v1/key/{id}</a>  ==> replace {id} with integer id<br>
                DELETE <a href="/api/v1/key/{id}">/api/v1/key/{id}</a>  ==> replace {id} with integer id<br>
                
        """,
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/' , include('api.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)