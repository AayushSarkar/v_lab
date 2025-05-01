from django.urls import path
from . import views

urlpatterns = [
    path('', views.youngs_double_slit, name='home'),  # Add this line
    path('youngs-double-slit/', views.youngs_double_slit, name='youngs_double_slit'),
]
