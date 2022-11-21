from django.test import TestCase
from django.urls import reverse

from feedback.models import Feedback
from feedback.forms import FeedbackForm


class FeedbackFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_form_context(self):
        response = self.client.get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], FeedbackForm)

    def test_text_label(self):
        text_label = FeedbackFormTest.form.fields['text'].label
        self.assertEqual(text_label, 'Текст')

    def test_text_help_text(self):
        text_label = FeedbackFormTest.form.fields['text'].help_text
        self.assertEqual(text_label, 'Введите отзыв')

    def test_create_task(self):
        feedbacks_count = Feedback.objects.count()
        form_data = {
            'text': 'Test',
        }
        response = self.client.post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, reverse('feedback:feedback'))
        self.assertEqual(Feedback.objects.count(), feedbacks_count + 1)
        self.assertTrue(
            Feedback.objects.filter(
                text='Test',
            ).exists()
        )
