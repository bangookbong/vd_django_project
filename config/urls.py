from django.contrib import admin
from django.urls import path, include
from chart import views as chart_views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', chart_views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('chart/', include('chart.urls')),

]
