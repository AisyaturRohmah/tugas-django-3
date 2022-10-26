from django.contrib import admin
from django.urls import path
from arastore.views import katalog,pricelist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('katalog/' ,katalog),
    path('pricelist/' ,pricelist),
    

]
