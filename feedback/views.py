from django.shortcuts import render, redirect
from django.core.mail import send_mail

from feedback.models import FeedbackForm


def feedback(request):
    template = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        send_mail(
            'Тема письма',
            form.cleaned_data['text'],
            'from@example.com',
            ['to@example.com', ],
            fail_silently=False,
        )
        redirect('feedback:feedback')
    return render(request, template, context)
