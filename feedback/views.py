from django.shortcuts import render, redirect
from django.core.mail import send_mail

from feedback.models import Feedback, FeedbackForm


def feedback(request):
    template = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        description = form.cleaned_data['text']
        send_mail(
            'Тема письма',
            description,
            'from@example.com',
            ['to@example.com', ],
            fail_silently=False,
        )
        Feedback.objects.create(text=description)
        return redirect('feedback:feedback')
    return render(request, template, context)
