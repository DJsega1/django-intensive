from functools import wraps
from re import search
from django.core.exceptions import ValidationError


def item_text_validator(*params):
    MIN_TEXT_LENGHT = 2

    @wraps(item_text_validator)
    def validate(value):
        words = [r'\b{}\b'.format(i) for i in params]
        value = value.lower()
        if len(value.split(' ')) <= MIN_TEXT_LENGHT:
            raise ValidationError('В описании должны быть больше 2-ух слов.')
        for i in words:
            if search(i, value):
                done = True
                break
        if not done:
            raise ValidationError(f'В описании должны быть слова {", ".join(params)}.')
    return validate
