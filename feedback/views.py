from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from feedback.models import Feedback
from feedback.forms import FeedbackForm


def feedback(request):
    template = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        description = form.cleaned_data['text']
        Feedback.objects.create(text=description)
        send_mail(
            'Тема письма',
            description,
            settings.SERVER_EMAIL,
            [settings.ADMIN_EMAIL, ],
            fail_silently=False,
        )
        return redirect('feedback:feedback')
    return render(request, template, context)
