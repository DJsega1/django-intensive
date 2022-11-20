from django.db import models
from django.forms import ModelForm, Textarea


class Feedback(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('text', )
        labels = {
            'text': 'Текст',
        }
        help_texts = {
            'text': 'Введите отзыв',
        }
        widgets = {
            'text': Textarea(attrs={
                'rows': '20',
                'cols': '80',
                'style': "resize: none",
                }),
        }
