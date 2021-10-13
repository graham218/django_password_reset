from django.urls import path
from reset import views

app_name = "reset"

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.home, name="home"),
    path('employees', views.employees, name="employees"),
    path('search_employees', views.search_employees, name='search_employees'),
    path('dns_lookup', views.dns_lookup, name='dns_lookup'),
]
