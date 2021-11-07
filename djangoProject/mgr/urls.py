from django.contrib import admin
from django.urls import path
from mgr import customer, medicine
from mgr import sign_in_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers', customer.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
    path('medicines', medicine.dispatcher)

]