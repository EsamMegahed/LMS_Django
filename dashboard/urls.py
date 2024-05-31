
from django.urls import path
from . import views
appname = 'dashboard'
urlpatterns = [
    path('', views.dash,name='users_view'),
    path('details/<int:id>', views.user_detail,name='details'),
    path('update/<int:id>', views.user_update,name='update'),   
    path('create_user/', views.create_user,name='create_user'), 


]
