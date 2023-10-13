from django.urls import path
from . import views
from .views import Propertyhomepage , Propertydetailpage , Agents ,Listings , Inquirylist

urlpatterns = [
    path("", Propertyhomepage.as_view() , name="property"),
    path("property/<str:pk>", Propertydetailpage.as_view(), name="propertydetailpage"),
    path("agent/", Agents.as_view(), name="agent"),
    path("listings/", Listings.as_view(), name="listing"),
    path("inquiry/", Inquirylist.as_view(), name="inquiry"),
]
