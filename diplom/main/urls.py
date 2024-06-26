from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('prices', views.prices, name='prices'),
    path('reiting', views.reiting, name='reiting'),
    path('contacts', views.contacts, name='contacts'),
    path('forma', views.Zakaz_view, name='forma'),
    path('forma1', views.forma1, name='forma1'),
    path("profile", views.profile, name="profile"),
    path("about", views.about, name="about"),
    path('zapisi', views.zapisi, name="zapisi"),
    path('sertificate', views.sertificate, name='sertificate'),
    path('workers', views.workers, name='workers'),
    path('zapros/', views.Zapros_View, name='zapros'),
    path('create_remont/', views.create_remont, name='create_remont'),
]