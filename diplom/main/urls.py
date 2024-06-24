from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('cources', views.cources, name='cources'),
    path('prices', views.prices, name='prices'),
    path('reiting', views.reiting, name='reiting'),
    path('contacts', views.contacts, name='contacts'),
    path('forma', views.Zakaz_view, name='forma'),
    path('forma1', views.forma1, name='forma1'),
    path("profile", views.profile, name="profile"),
    path("profile-courses", views.profile_courses, name="profile-courses"),
    path("about", views.about, name="about"),
    path('course1', views.course1, name='course1'),
    path('course2', views.course2, name='course2'),
    path('course3', views.course3, name='course3'),
    path('modules1', views.module, name='modules1'),
    path('zapisi', views.schedule, name="zapisi"),
    path('sertificate', views.sertificate, name='sertificate'),
    path('workers', views.workers, name='workers'),
]