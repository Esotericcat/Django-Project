from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'home.html')


class TaskCreateView(View):
    def get(self, request):

        return render(request, 'task_create.html')

    def post(self, request):
        pass
