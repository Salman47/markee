from django.db.models import Q
from collections import Counter
from account.models import User
from django.contrib import messages
from operations.models import Task, ToDoItem
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from operations.forms import TaskForm, ToDoForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseNotAllowed


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('sign-in')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password Incorrect')

    return render(request, 'pages/samples/login.html', {'page': 'signin'})


def sign_out(request):
    logout(request)
    return redirect('sign-in')


def sign_up(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'pages/samples/register.html', {'form': form})

            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()

            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Error occurred during registration.')

    return render(request, 'pages/samples/register.html', {'form': form})


def home(request):
    task_list = Task.objects.all()
    todoitems = ToDoItem.objects.all()

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    task_list = Task.objects.filter(
        Q(task_number__icontains=q) |
        Q(client_name__icontains=q) |
        Q(fotoage_link__icontains=q) |
        Q(approval_status__icontains=q)
    )

    return render(
        request, 'body.html',
        {
            'task_list': task_list,
            'todoitems': todoitems,
        }
    )


def create_task(request):
    doc = "Add New Task"
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')

    return render(request, 'pages/tasks/tasks.html', {'form': form, 'doc_name': doc})


def update_task(request, pk):
    doc = "Update Task"
    task = Task.objects.get(task_number=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'pages/tasks/tasks.html', {'form': form, 'doc_name': doc})


def delete_task(request, pk):
    task = Task.objects.get(task_number=pk)
    task.delete()
    return redirect('/')


def create_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('/')

    return render(request, 'body.html')


def update_todo(request, pk):
    todo = ToDoItem.objects.get(id=pk)
    form = ToDoForm(instance=todo)

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'form.html', {'form': form})


def delete_todo(request, pk):
    todo = ToDoItem.objects.get(id=pk)
    todo.delete()
    return redirect('/')


def doughnut_plot(request):
    tasks = Task.objects.filter(user=request.user)
    approvals = [task.approval_status for task in tasks]

    context = {}
    status = Counter(approvals)

    context['rejected'] = status['Rejected']
    context['approved'] = status['Approved']
    context['pending'] = status['Pending']

    return JsonResponse(context)


def areachart(request):
    tasks = Task.objects.filter(user=request.user)

    context = {}
    assigned = [0] * 12
    completed = [0] * 12

    for task in tasks:
        month = task.start_date.month - 1
        assigned[month] += 1

        if task.approval_status == 'Approved':
            completed[month] += 1

    context = {
        'assigned': assigned,
        'completed': completed
    }

    return JsonResponse(context)
