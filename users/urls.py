from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from users import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name=''), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name=''), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name=''), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name=''), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name=''), name='password_reset_done'),
    path('password_reset_confirm/', PasswordResetConfirmView.as_view(template_name=''), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name=''), name='password_reset_complete')
]
