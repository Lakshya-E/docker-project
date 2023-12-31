from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.details, name='details'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signip'),
]
