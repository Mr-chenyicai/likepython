from django.contrib import admin
from django.urls import path
from sales.views import listorders, listcustomers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', listorders),
    path('customers/', listcustomers),
]