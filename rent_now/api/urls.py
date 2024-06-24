from django.urls import path , include 
from .views import AddressListUpdateView , CategoryListCreateView , RentRequestListCreateView , RentPostListView , RentPostCreateView , RentPostGetSingleView , RentOrderCreateView , RentOrderGetUpdateSingleView , RentOrderListView , RentOrderListOwnerUserView


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
    path(
        "users/<int:user_id>/rent-order/create/",
        RentOrderCreateView.as_view(),
        name="rent-post-create",    
    ),
    path(
        "rent-order/<int:pk>/",
        RentOrderGetUpdateSingleView.as_view(),
        name="rent-order-view",    
    ),
    path(
        "users/<int:user_id>/rent-order/",
        RentOrderListView.as_view(),
        name="rent-order-list-view",    
    ),
    path(
        "users/<int:user_id>/rent-order/owner-user/",
        RentOrderListOwnerUserView.as_view(),
        name="rent-order-list-owner-user-view",    
    ),

    
 ] 