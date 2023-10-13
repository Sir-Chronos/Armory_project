from django.urls import path
from armory.views.user import UserView
from armory.views.userRequest import UserRequestView
from armory.views.cabinet import CabinetView
from armory.views.log import LogView

urlpatterns = [
    path('api/users/', UserView.as_view()),  # Route to handle users (GET and POST)
    path('api/users/<int:id>/', UserView.as_view()),  # Route to handle a user by ID (PUT and DELETE)
    path('api/users/validate/<str:token>/<int:cabinet>', UserRequestView.as_view()),  # Route to validate user access
    path('api/cabinets/', CabinetView.as_view()),  # Route to handle cabinets (GET and POST)
    path('api/cabinets/<int:id>/', CabinetView.as_view()),  # Route to handle a cabinet by ID (PUT and DELETE)
    path('api/logs/', LogView.as_view()),  # Route to handle logs (GET and POST)
]
