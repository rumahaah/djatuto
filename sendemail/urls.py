from django.urls import path

from . import views

urlpatterns = [
    path('', views.sendemail, name='sendemail'),
    path('form', views.sendemailform, name='sendemailform'),
    # path('detail', views.detail, name='detail'),
    path('email/<slug:emailto>', views.sendSimpleEmail),
]