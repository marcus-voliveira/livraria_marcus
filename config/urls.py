from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria_marcus.views import CategoriaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
