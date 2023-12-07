from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/main_menu.html', takes_context=False)
def draw_menu(menu_name):
    menu_items = MenuItem.objects.all().filter(name=menu_name).get_descendants(include_self=False)
    return {
        "menu_id": menu_items,
    }


