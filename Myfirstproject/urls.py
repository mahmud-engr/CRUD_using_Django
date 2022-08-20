from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),

]
