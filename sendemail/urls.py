from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cc/<slug:paramm>', views.index),
    path('sendemail/<int:pk>', views.sendemail, name='sendemail'),
    # path('form', views.sendemailform, name='sendemailform'),
    # path('detail', views.detail, name='detail'),
    # path('email/<slug:emailto>', views.sendSimpleEmail),
    # path('form/create/', views.form_create, name='form_create'),
]