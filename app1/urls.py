from django.conf.urls import url
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home),
    path('caccount/', views.registration, name='account'),
    path('caccount/reg_upload/', views.reg_upload, name='reg_upload'),
    path('dash_board/', views.dash_board, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    #path('rest/', views.UserList.as_view()),
    path('act/',views.ActivityListView.as_view()),
]
