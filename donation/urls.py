from django.urls import path
from . import views

urlpatterns = [
    # your other URLs
    path('donation/',views.donationView.as_view()),
    path('searchBlood/<str:blood_type>/',views.searchDonarUsingBloodType.as_view()),
    path('doanteDetails/<int:pk>/',views.donateCardDetails.as_view()),
    path('bloodRequest/',views.requestBloddApiView.as_view()),
    path('requestOfuser/<int:pk>/',views.bloodRequestShowingByuserId.as_view())
]
