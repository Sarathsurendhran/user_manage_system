from django.urls import path
from .views import *

urlpatterns = [
  path('hotel-booking/<int:id>/', ProtectedView.as_view()),
  path('flight-booking/<int:id>/', ProtectedView.as_view()),
  path('assistant-hotel-booking/<int:id>/', RoleView.as_view()),
  path('assistant-flight-booking/<int:id>/', RoleView.as_view()),
]