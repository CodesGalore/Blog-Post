from django.urls import path
from .views import homepage,momentinformation,addingamoment,updateamoment,deleteamoment
from . import views

urlpatterns = [
    path('', homepage.as_view(), name ="home"),
    path('moment/<int:pk>',momentinformation.as_view(), name="moment-information"),
    path('addmoment/',addingamoment.as_view(),name = "add_mymoment"),
    path('moment/update/<int:pk>',updateamoment.as_view(),name = "update_moment"),
    path('moment/<int:pk>/delete',deleteamoment.as_view(),name = "delete_moment"),

    
]