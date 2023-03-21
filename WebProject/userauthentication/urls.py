from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetDoneView
from .views import CustomPasswordResetCompleteView
from .views import CustomPasswordResetConfirmView
#from .views import SignUp
from .import views





#urlpatterns = [
#    path('signup/',SignUp.as_view(),name = 'sign_up'),
#]

#app_name = "userauthentication"

urlpatterns = [
    path('signup/',views.register_request,name = 'sign_up'),

    path('password-reset-done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'), 

    path("password_reset", views.password_reset_request, name="password_reset")


   


]