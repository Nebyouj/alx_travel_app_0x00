from django.urls import path
from . import views  # or your view imports

urlpatterns = [
    # example path; replace with your actual views
    path('', views.index, name='index'),
]
