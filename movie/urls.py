from django.urls import include, path

from rest_framework import routers

from .views import MovieViewSet

router = routers.DefaultRouter()

router.register(r'movie', MovieViewSet, 'movie-detail')

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
