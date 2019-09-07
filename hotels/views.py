from datetime import datetime

#error
from rest_framework.generics import ListAPIView, CreateAPIView ,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Hotel
from .permissions import IsBookedByUser, IsNotInPast
from .serializers import HotelsListSerializer, HotelDetailsSerializer, BookHotelSerializer, BookingDetailsSerializer, UserSerializer, UserCreateSerializer


class HotelsList(ListAPIView):
	queryset = Hotel.objects.all()
	serializer_class = HotelsListSerializer
	filter_backends = [SearchFilter,]
	search_fields = ['name', 'location']


class HotelDetails(RetrieveAPIView):
	queryset = Hotel.objects.all()
	serializer_class = HotelDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'hotel_id'


class BookingsList(ListAPIView):
	serializer_class = BookingDetailsSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		today = datetime.today()
		#error .filter not .get
		return Booking.objects.filter(user=self.request.user, check_in__gte=today)


class BookHotel(CreateAPIView):
	serializer_class = BookHotelSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, hotel_id=self.kwargs['hotel_id'])


class ModifyBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookHotelSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'	
	permission_classes = [IsBookedByUser, IsNotInPast]


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	#error
	lookup_url_kwarg = 'booking_id'
	permission_classes = [IsBookedByUser, IsNotInPast]


class Profile(RetrieveAPIView):
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user


class Register(CreateAPIView):
    serializer_class = UserCreateSerializer




