from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# defining routers
router = DefaultRouter()
router.register("", views.GSMViewSet, basename="GSMViewSet")

urlpatterns = [
    path("",views.Hello),
    path("api", include(router.urls)),



]
