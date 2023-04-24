import random

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Trainer
from django.contrib.auth.models import User

class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'blog_post_user_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')

class MainPageView(View):
    template_name = 'main_page.html'
    def get(self, request):
        return render (request, self.template_name)

class TrainersListView(ListView):
    model = Trainer
    template_name = 'trainers_list.html'
    context_object_name = 'trainers'



class LogInUser(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # обработка POST-запроса с данными для входа
        return render(request, 'login.html')



class TrainerPageView(View):
    def get(self, request, trainer_id):
        trainer = get_object_or_404(Trainer, pk=trainer_id)
        context = {'trainer': trainer}
        return render(request, 'trainer.html', context)


class AttendanceView(View):
    def get(self, request, *args, **kwargs):
        random_num = random.randint(1, 100)
        return render(request, 'attendance.html', {'random_number': random_num})


