"""booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) #error

from rest_framework_jwt.views import obtain_jwt_token

from hotels import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hotels/list/', views.HotelsList.as_view(), name="hotels-list"),
    path('hotels/details/<int:hotel_id>/', views.HotelDetails.as_view(), name="hotel-details"), #error
    path('hotels/book/<int:hotel_id>/', views.BookHotel.as_view(), name="book-hotel"),

    path('bookings/', views.BookingsList.as_view(), name="bookings-list"),
    path('bookings/cancel/<int:booking_id>/', views.CancelBooking.as_view(), name="cancel-booking"),
    path('bookings/modify/<int:booking_id>/', views.ModifyBooking.as_view(), name="modify-booking"),

    path('profile/', views.Profile.as_view(), name="profile"), #error

    path('login/', TokenObtainPairView.as_view(), name="login"), #error
    path('register/',  views.Register.as_view() , name="register"),
]
