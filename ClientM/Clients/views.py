# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, SubscriptionAssignment, Subscription, Project, Task
from .forms import ClientForm,UserProfileForm, ProjectForm, SubscriptionForm,SubscriptionAssignmentForm, TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client/client_form.html', {'form': form})

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_view', pk=pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/client_form.html', {'form': form})

@login_required
def client_view(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client/client_view.html', {'client': client})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client/client_confirm_delete.html', {'client': client})

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project/project_form.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'project/project_confirm_delete.html', {'project': project})

@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscription/subscription_list.html', {'subscriptions': subscriptions})

@login_required
def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'subscription/subscription_form.html', {'form': form})

@login_required
def subscription_edit(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=subscription)
    return render(request, 'subscription/subscription_form.html', {'form': form})

@login_required
def subscription_delete(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription_list')
    return render(request, 'subscription/subscription_confirm_delete.html', {'subscription': subscription})

@login_required
def subscription_assignment_list(request):
    subscription_assignments = SubscriptionAssignment.objects.all()
    return render(request, 'subscriptionAssin/subscription_assignment_list.html', {'subscription_assignments': subscription_assignments})

@login_required
def subscription_assignment_create(request):
    if request.method == 'POST':
        form = SubscriptionAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_assignment_list')
    else:
        form = SubscriptionAssignmentForm()
    return render(request, 'subscriptionAssin/subscription_assignment_form.html', {'form': form})

@login_required
def subscription_assignment_edit(request, pk):
    subscription_assignment = get_object_or_404(SubscriptionAssignment, pk=pk)
    if request.method == 'POST':
        form = SubscriptionAssignmentForm(request.POST, instance=subscription_assignment)
        if form.is_valid():
            form.save()
            return redirect('subscription_assignment_list')
    else:
        form = SubscriptionAssignmentForm(instance=subscription_assignment)
    return render(request, 'subscriptionAssin/subscription_assignment_form.html', {'form': form})

@login_required
def subscription_assignment_delete(request, pk):
    subscription_assignment = get_object_or_404(SubscriptionAssignment, pk=pk)
    if request.method == 'POST':
        subscription_assignment.delete()
        return redirect('subscription_assignment_list')
    return render(request, 'subscriptionAssin/subscription_assignment_confirm_delete.html', {'subscription_assignment': subscription_assignment})


@login_required
def view_profile(request):
    user_profile = request.user.userprofile
    return render(request, 'view_profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})