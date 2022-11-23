from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile-update/', views.profile_update, name='profile_update'),
	path('follow/', views.users_follow, name='follow'),
    path('password-change/',
		auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'),
		name='password_change'),
	path('password-change/done/',
		auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
		name='password_change_done'),
	# reset password urls
	path('password-reset/',
		auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'),
		name='password_reset'),
	path('password-reset/done/',
		auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
		name='password_reset_done'),
	path('reset/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
		name='password_reset_confirm'),
	path('reset/done/',
		auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
		name='password_reset_complete'),
]