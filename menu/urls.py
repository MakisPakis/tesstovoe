from django.urls import path
from .views import MenuItemListView, MenuVehicleListView, MenuLoaderListView, MenuTruckListView

urlpatterns = [
    path('', MenuItemListView.as_view(), name='home'),
    path('vehicle/', MenuVehicleListView.as_view(), name='vehicle'),
    path('loader/', MenuLoaderListView.as_view(), name='loader'),
    path('truck/', MenuTruckListView.as_view(), name='truck'),
    ]
