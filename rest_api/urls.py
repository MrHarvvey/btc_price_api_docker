from django.urls import path
from .views import safe_people2, bitcoin_cost

urlpatterns = [
	#Leave as empty string for base url
	path('zadanie1/', safe_people2, name='safepeople2'),
	path('zadanie2/', bitcoin_cost, name='safepeople3'),
]
