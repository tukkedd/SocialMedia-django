
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PublicacionViewSet, LikeViewSet, ComentarioViewSet, AmistadViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('publicaciones', PublicacionViewSet)
router.register('likes', LikeViewSet)
router.register('comentarios', ComentarioViewSet)
router.register('amistades', AmistadViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

 