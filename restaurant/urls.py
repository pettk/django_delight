from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('inventory', views.inventory),
    path('menu', views.menu),
    path('recipe', views.recipe),
    path('purchase_log', views.purchase_log),
    path('update_inventory', views.add_inventory),
    path('update_inventory/<inv_id>', views.update_inventory),
    path('delete/<inv_id>', views.delete)
]