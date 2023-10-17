from django.urls import path

from . import views
 
app_name = 'items'

urlpatterns = [
    path('', views.search, name='search'),
    path('new/', views.newItem, name='new'),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),\
    path('<int:pk>/edit/', views.editItem, name="edit"),
 
]
