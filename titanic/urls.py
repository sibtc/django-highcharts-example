"""titanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from passengers import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ticket-class/', views.ticket_class_view, name='ticket_class'),
    path('ticket-class/2/', views.ticket_class_view_2, name='ticket_class_2'),
    path('ticket-class/3/', views.ticket_class_view_3, name='ticket_class_3'),
    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),
    path('admin/', admin.site.urls),
]
