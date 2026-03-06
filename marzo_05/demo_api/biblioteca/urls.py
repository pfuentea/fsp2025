from rest_framework.routers import DefaultRouter
from .views import AutorViewSet,LibroViewSet

router = DefaultRouter()

router.register('autores',AutorViewSet)
router.register('libros',LibroViewSet)

urlpatterns=router.urls