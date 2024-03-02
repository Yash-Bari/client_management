# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/new/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
     path('clients/<int:pk>/view/', views.client_view, name='client_view'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/new/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('subscriptions/new/', views.subscription_create, name='subscription_create'),
    path('subscriptions/<int:pk>/edit/', views.subscription_edit, name='subscription_edit'),
    path('subscriptions/<int:pk>/delete/', views.subscription_delete, name='subscription_delete'),
    path('subscription-assignments/', views.subscription_assignment_list, name='subscription_assignment_list'),
    path('subscription-assignments/new/', views.subscription_assignment_create, name='subscription_assignment_create'),
    path('subscription-assignments/<int:pk>/edit/', views.subscription_assignment_edit, name='subscription_assignment_edit'),
    path('subscription-assignments/<int:pk>/delete/', views.subscription_assignment_delete, name='subscription_assignment_delete'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
