from django.urls import path
from inventario import views
from rest_framework.routers import DefaultRouter

app_name = "inventario"

router = DefaultRouter()
router.register(r'equipo', views.EquipoViewSet, basename='equipo')
router.register(r'equipo-usuario', views.EquipoUsuarioViewSet, basename='equipo-usuario')

urlpatterns = [
    path("get-all-equipos/", views.GetAllEquiposAPIView.as_view(), name="get-all-equipos"),
]

urlpatterns += router.urls