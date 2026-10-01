"""
URL configuration for care_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from staff.views import DoctorListCreateView
from staff.views import DoctorRetrieveUpdateDeleteView
from staff_v2 import views
from staff_v2.views import AdminCreateView
from bookings.views import AppointmentsListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("doctors/",DoctorListCreateView.as_view()),
    path("doctors/<int:pk>/",DoctorRetrieveUpdateDeleteView.as_view()),

    #v2 route

    path("v2/doctors/",views.DoctorListCreateView.as_view()),
    path("v2/doctors/<int:pk>/",views.DoctorRetrieveUpdateDeleteView.as_view()),

    #v2 admin-register route

    path("v2/admin-register/",views.AdminCreateView.as_view()),

    #bookings route

    path("bookings/",AppointmentsListCreateView.as_view())
]
