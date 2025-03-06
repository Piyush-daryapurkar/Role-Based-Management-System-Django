from django.urls import path
from . import views

urlpatterns = [
    path("",views.animesh,name=""),
    path("super",views.Superdashboard,name="super"),
    path("Manager_login",views.Manager_login,name="Manager_login"),
    path("/image",views.manager_update_profile,name="image")
]