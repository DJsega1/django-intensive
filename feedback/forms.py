from django.forms import ModelForm, Textarea

from feedback.models import Feedback


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
        # TODO: refactor
        widgets = {
            'text': Textarea(attrs={
                'rows': '20',
                'cols': '80',
                'style': "resize: none",
                }),
        }
