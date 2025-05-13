from django.conf.urls.static import static
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.i18n import set_language
from root import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = i18n_patterns(
       path('admin/', admin.site.urls),
       path('api-auth/', include('rest_framework.urls')),
       path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
       path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
       path('user/',include('user.urls')),
       path('orders/',include('orders.urls')),
       path('properties/',include('properties.urls')),
       path('reviews/',include('reviews.urls')),

    #JWT token url
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



)
urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

