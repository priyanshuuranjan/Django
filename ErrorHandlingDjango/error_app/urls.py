from django.urls import path
from .import views 
urlpatterns = [
    path("successful/", views.successful),
    path('created/', views.created),
    path('accepted/', views.accepted),
    path('found/', views.found),
    #path('bad-request/',views.bad-request),
]
