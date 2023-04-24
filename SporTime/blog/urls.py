
from django.urls import path, re_path

from blog.views import UserPostListView, MainPageView, TrainersListView, LogInUser, TrainerPageView, AttendanceView

urlpatterns = [

    path('posts/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list' ),
    path('',MainPageView.as_view(), name='main_page'),
    path('trainers_list/', TrainersListView.as_view(), name='trainers_list'),
    path('login/',LogInUser.as_view(), name='login'),
    path('trainer/<int:trainer_id>/', TrainerPageView.as_view(), name='trainer' ),
    path('attendance/', AttendanceView.as_view(), name='attendance'),
]

