from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, DealerViewSet, OrderViewSet, InventoryViewSet
from . import views


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'dealers', DealerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'inventory', InventoryViewSet)


urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('inventory/', views.inventory, name='inventory'),

    path('delete-inventory/<int:id>/', views.delete_inventory),

    path('create-order/', views.create_order, name='create_order'),

    path('dealers/', views.dealers_page, name='dealers'),

    path('orders/', views.orders_page, name='orders'),  # ADD THIS

    path('track-order/<int:id>/', views.track_order, name='track_order'),

    path('api/', include(router.urls)),
]