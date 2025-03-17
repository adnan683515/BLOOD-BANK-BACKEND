from django.urls import path
from . import views

urlpatterns = [
    # your other URLs
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('userdetails/',views.userDetalisView.as_view()),
    path('logout/',views.logoutView.as_view()),
    path('DetailsUserView/<int:pk>/',views.DetailsUserView.as_view())
    
]
