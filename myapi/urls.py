# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet, basename='items')
router.register(r'mensitems', views.ItemMensViewSet, basename='mensitems')
router.register(r'womensitems', views.ItemWomensViewSet, basename='womensitems')
router.register(r'category', views.ItemCategoriesViewSet, basename='category')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
