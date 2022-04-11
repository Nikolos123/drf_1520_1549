from django.urls import path
from .views import UserListApiView

app_name = 'userapp'

urlpatterns = [

    path('',UserListApiView.as_view()),

]