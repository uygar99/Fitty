"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from general import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  url(r'^$', views.HomeView.as_view(), name='home'),
                  url(r'^trainer/(?P<user_id>\d+)/$', views.TrainerProfileView.as_view(), name="trainer_profile"),
                  url(r'^delete_workout/(?P<id>\d+)/$', views.DeleteWorkoutView.as_view(), name="delete_workout"),
                  url(r'^ajax_add_workout/$', views.AjaxAddWorkoutView.as_view(), name="ajax_add_workout"),
                  url(r'^ajax_status/$', views.AjaxStatusView.as_view(), name="ajax_status"),
                  url(r'^stats/$', views.StatView.as_view(), name='stats'),
                  url(r'^trainers/$', views.TrainerView.as_view(), name='trainers'),
                  url(r'^schedule/$', views.ScheduleView.as_view(), name='schedule'),
                  url(r'^add_workout/$', views.AddWorkoutView.as_view(), name='add_workout'),
                  url(r'^account/trainer$', views.TrainerAccountView.as_view(), name='trainer_account'),
                  url(r'^tdee_calculation$', views.TDEEView.as_view(), name='tdee_calculation'),
                  url(r'^account/edit_trainer$', views.EditTrainerAccountView.as_view(), name='edit_trainer'),
                  url(r'^edit_stats$', views.EditStatsView.as_view(), name='edit_stats'),
                  url(r'^workouts/$', views.WorkoutsView.as_view(), name='workouts'),
                  url(r'^workout/(?P<id>\d+)/$', views.WorkoutView.as_view(), name='workout'),
                  url(r'^account/trainee$', views.TraineeAccountView.as_view(), name='trainee_account'),
                  url(r'^signup/$', accounts_views.SignUp.as_view(), name='signup'),
                  url(r'^signup/trainer$', accounts_views.TrainerSignUp.as_view(), name='signup_trainer'),
                  url(r'^signup/trainee$', accounts_views.TraineeSignUp.as_view(), name='signup_trainee'),
                  url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
                  url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^settings/password/$',
                      auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
                      name='password_change'),
                  url(r'^settings/password/done/$',
                      auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
                      name='password_change_done'),
                  url(r'^reset/$',
                      auth_views.PasswordResetView.as_view(
                          template_name='password_reset.html',
                          email_template_name='password_reset_email.html',
                          subject_template_name='password_reset_subject.txt'
                      ),
                      name='password_reset'),
                  url(r'^reset/done/$',
                      auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                      name='password_reset_done'),
                  url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                      auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
                      name='password_reset_confirm'),
                  url(r'^reset/complete/$',
                      auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
                      name='password_reset_complete'),
                  url('accounts/reset/done/',
                      auth_views.PasswordResetDoneView.as_view(template_name='password_reset_complete.html'),
                      name='reset_done'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
