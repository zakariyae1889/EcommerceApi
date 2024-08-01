
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/products/', include("Products.urls")),
    path('api/order/', include("Order.urls")),
    path('api/client/', include("Client.urls")),
    path("api/checkout/",include("checkout.urls")),
    path('api/payment/', include("Payment.urls")),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

handler404='utils.error_views.handler_404'
handler500='utils.error_views.handler_500'