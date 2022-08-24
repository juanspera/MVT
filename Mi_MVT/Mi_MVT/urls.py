from django.contrib import admin
from django.urls import path
from Family.views import ver_familia

urlpatterns = [
    path('admin/', admin.site.urls),
  ##  path('home/',home)
  path('familia/',ver_familia)
]
