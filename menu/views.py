from django.views.generic import ListView
from .models import MenuItem


class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menu/index.html'
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тестовое задание'
        return context


class MenuVehicleListView(ListView):
    model = MenuItem
    template_name = 'menu/vehicle.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'спецтехника'
        return context


class MenuLoaderListView(ListView):
    model = MenuItem
    template_name = 'menu/loader.html'
    context_object_name = 'loader'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Погрузчик'
        return context


class MenuTruckListView(ListView):
    model = MenuItem
    template_name = 'menu/truck.html'
    context_object_name = 'truck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Самосвал'
        return context