from django.urls import include, path
from .views import getPhoneNumber, getPhoneNumber_TimeBased

urlpatterns = [
    path("<phone>/", getPhoneNumber.as_view(), name= "New OTP"),
    path("timer/<phone>/", getPhoneNumber_TimeBased.as_view(), name= "Timer OTP"),
]

