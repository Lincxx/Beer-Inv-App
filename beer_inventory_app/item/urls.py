from django.urls import path

from . import views

# namespace for app
app_name = 'item'

urlpatterns = [
    path('', views.browse, name='browse'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete_item, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),

]
