from django.urls import path , include 
from .views import AddressListUpdateView , CategoryListCreateView , RentRequestListCreateView , RentPostListView , RentPostCreateView , RentPostGetSingleView


urlpatterns = [
    
    path(
        "users/<int:user_id>/addresses/",
        AddressListUpdateView.as_view(),
        name="address-create-get",    
    ),
    path(
        "categories/",
        CategoryListCreateView.as_view(),
        name="category-create-get", )   , 
    path(
        "rent-request/",
        RentRequestListCreateView.as_view(),
        name="rentrequest-create-get", )   , 
    path(
        "users/<int:user_id>/rent-post/",
        RentPostListView.as_view(),
        name="rent-post-get",    
    ),
    path(
        "users/<int:user_id>/rent-post/create/",
        RentPostCreateView.as_view(),
        name="rent-post-create",    
    ),
    path(
        "rent-post/<int:pk>/",
        RentPostGetSingleView.as_view(),
        name="rent-single-view",    
    ),
    
 ] 