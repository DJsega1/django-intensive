from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from users import views

urlpatterns = [
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),
    path('login/',
         LoginView.as_view(
             template_name='users/login.html',
         ),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
    path('password_change/',
         PasswordChangeView.as_view(
             template_name='users/password_change.html'
         ),
         name='password_change'),
    path('password_change_done/',
         PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'
         ),
         name='password_change_done'),
    path('password_reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('users/', views.user_list, name='user-list'),
    re_path(r'^users/(?P<pk>[1-9]\d*)/$',
            views.user_detail,
            name='user-detail'),
    path('profile/', views.profile, name='profile')
]
