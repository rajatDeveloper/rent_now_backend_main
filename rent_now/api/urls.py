from django.urls import path , include 
from .views import AddressListUpdateView

urlpatterns = [
     path(
        "users/<int:user_id>/addresses/",
        AddressListUpdateView.as_view(),
        name="address-create-get",
    ),
 ] 