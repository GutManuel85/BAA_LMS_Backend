from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_courses),
    path('categories/', views.get_categories),
    path('user-profile/', views.get_user_profile),
    path('my-courses/', views.get_my_courses),
    path('ranking/', views.get_ranking_data),
    path('add-points/<int:points_to_add>/', views.add_points),
    path('<slug:slug>/', views.get_course),
]
