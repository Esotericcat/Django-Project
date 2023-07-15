from django.shortcuts import render
from django.views import View
from to_do_app.models import ToDolist
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


class TaskCreateView(View):
    def get(self, request):

        return render(request, 'task_create.html')

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        to_date = request.POST.get('date')
        ToDolist.objects.create(name=name, description=description, to_date=to_date)
        td = ToDolist()
        td.save()
        messages.success(request, f'task {name} added successfully!')




        return render(request, 'task_create.html')

