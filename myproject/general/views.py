import json

import Listing as Listing
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from general.forms import AddWorkoutForm

from general.forms import EditTrainerForm

from general.forms import EditTrainerUsernameForm

from general.forms import AddImageForm

from general.forms import EditStatisticsForm
from .models import Workout, Trainer, Status
from .models import Trainee
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, request, *args, **kwargs):
        trainers = Trainer.objects.all()
        paginator = Paginator(trainers, 6)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        return render(request, 'home.html', context={"page": page})


class StatView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trainee = request.user.trainee
        return render(request, 'stats.html', context={"trainee": trainee})


class TrainerView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trainers = Trainer.objects.all()
        paginator = Paginator(trainers, 12)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        return render(request, 'trainer.html', context={"page": page})


class TrainerAccountView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        wos = Workout.objects.filter(trainer=request.user.trainer)
        mydict = {'workouts': wos}
        return render(request, 'trainer_account.html', context=mydict)


class TraineeAccountView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trainee = request.user.trainee
        workout_list = trainee.workout_list
        mydict = {'workout_list': workout_list.all()}
        return render(request, 'trainee_account.html', context=mydict)


class AjaxAddWorkoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        workout = Workout.objects.filter(id=request.POST.get('workout_id'))[0]
        trainee = request.user.trainee
        print(workout.id)
        print(workout.pk)
        wo_list = trainee.workout_list
        print(wo_list)
        if workout in wo_list.all():
            trainee.workout_list.remove(workout)
            is_added = False
        else:
            trainee.workout_list.add(workout)
            status = Status.objects.create()
            status.trainee = trainee
            status.workout = workout
            status.save()
            is_added = True
        context = {'is_added': is_added}
        return HttpResponse(json.dumps(context), content_type='application/json')


class AjaxStatusView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        status_id = request.POST.get('status_id')
        print(status_id)
        status = Status.objects.filter(id=status_id)[0]
        if status.statuses == 'To Do':
            status.statuses = 'Done'
        else:
            status.statuses = 'To Do'
        status.save()
        context = {'statuses': status.statuses}
        return HttpResponse(json.dumps(context), content_type='application/json')


class ScheduleView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trainee = request.user.trainee
        workout_list = trainee.workout_list
        status_list = []
        for i in workout_list.all():
            status = Status.objects.filter(trainee=trainee, workout=i)
            status_list.append(status)
        zipped = list(zip(workout_list.all(), status_list))
        mydict = {'zipped': zipped}
        return render(request, 'schedule.html', context=mydict)


class EditStatsView(LoginRequiredMixin, View):
    model = Trainee

    def post(self, request, *args, **kwargs):
        form = EditStatisticsForm(request.POST)
        print("forma girmeden önce")
        if form.is_valid():
            print("forma girdi")
            trainee = form.save(commit=False)
            trainee.user = User.objects.get(id=request.user.id)
            form.save()
            messages.success(request, "You Added the Workout!")
            return redirect('stats')
        else:
            messages.error(request, "Workout did not save.")

    def get(self, request, *args, **kwargs):
        form = EditStatisticsForm()
        return render(request, 'edit_stats.html', context={'form': form})


class WorkoutsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        workouts = Workout.objects.all()
        is_added_list = []
        trainee = request.user.trainee
        wo_list = trainee.workout_list.all()
        for i in workouts:
            if i in wo_list:
                is_added_list.append(True)
            else:
                is_added_list.append(False)
        wo = {}
        for index, i in enumerate(workouts):
            t = (i, is_added_list[index])
            wo.setdefault(i.workout_type, []).append(t)
        print(wo)
        zipped = zip(wo, is_added_list)
        mydict = {'workouts': wo, 'zipped': zipped}
        return render(request, 'workouts.html', context=mydict)


class EditTrainerAccountView(LoginRequiredMixin, View):
    model = Trainer

    def post(self, request, *args, **kwargs):
        form = EditTrainerForm(request.POST, instance=request.user.trainer)
        username_form = EditTrainerUsernameForm(request.POST, instance=request.user)
        image_form = AddImageForm(request.POST, request.FILES, instance=request.user.trainer)
        print("forma girmeden önce")
        print(request.POST)
        if 'username_form' in request.POST and username_form.is_valid():
            username_form.save()
            return redirect("trainer_account")
        if 'form' in request.POST and form.is_valid():
            form.save()
            return redirect("trainer_account")
        if 'image_form' in request.POST and image_form.is_valid():
            image_form.save()
            return redirect("trainer_account")
        else:
            print("elseee")
            messages.error(request, "Changes did not save.")
            return render(request, 'trainer_edit_profile.html')

    def get(self, request, *args, **kwargs):
        form = EditTrainerForm()
        username_form = EditTrainerUsernameForm()
        image_form = AddImageForm()
        context = {
            'form': form,
            'username_form': username_form,
            'image_form': image_form,
        }
        return render(request, 'trainer_edit_profile.html', context)


class TDEEView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trainees = Trainee.objects.all()
        return render(request, 'tdee.html', context={"stats": trainees})


class WorkoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        workout_id = kwargs['id']
        workout = Workout.objects.get(id=workout_id)
        print(workout.name)
        return render(request, 'workout_page.html', context={'workout': workout})


class TrainerProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        user = User.objects.get(id=user_id)
        trainer = Trainer.objects.get(user=user)
        wos = Workout.objects.filter(trainer=user.trainer)
        if user == request.user:
            return redirect('trainer_account')
        return render(request, 'trainer_profiles.html', context={'trainer': trainer, 'workouts': wos})


class DeleteWorkoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        workout_id = kwargs['id']
        workout = Workout.objects.get(id=workout_id)
        workout.delete()
        return redirect('trainer_account')


class AddWorkoutView(LoginRequiredMixin, View):
    model = Workout

    def post(self, request, *args, **kwargs):
        form = AddWorkoutForm(request.POST, request.FILES)
        print("forma girmeden önce")
        if form.is_valid():
            print("forma girdi")
            workout_name = form.cleaned_data['name']
            working_muscles = form.cleaned_data['working_muscles']
            difficulty = form.cleaned_data['difficulty']
            workout_type = form.cleaned_data['workout_type']
            description = form.cleaned_data['description']
            photo = form.cleaned_data['photo']
            url = form.cleaned_data['url']
            trainer = request.user.trainer
            workout = Workout(name=workout_name, working_muscles=working_muscles, difficulty=difficulty,
                              workout_type=workout_type,
                              description=description, photo=photo, trainer=trainer, url=url)
            workout.save()
            messages.success(request, "You Added the Workout!")
            return redirect('add_workout')
        else:
            messages.error(request, "Workout did not save.")

    def get(self, request, *args, **kwargs):
        form = AddWorkoutForm()
        return render(request, 'add_workout.html', context={'form': form})
