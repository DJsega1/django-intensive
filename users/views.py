from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserCreationForm, UserChangeForm
from users.models import User


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def user_list(request):
    template = 'users/user_list.html'
    users = User.objects.active()
    context = {
        'users': users,
    }
    return render(request, template, context)


def user_detail(request, pk):
    template = 'users/user_detail.html'
    user = get_object_or_404(User.objects.active(), pk=pk)
    context = {
        'user': user,
    }
    return render(request, template, context)


@login_required
def profile(request):
    template = 'users/profile.html'
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, template, context)
