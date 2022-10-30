from functools import wraps
from django.core.exceptions import ValidationError


def item_text_validator(*params):
    @wraps(item_text_validator)
    def validate(value):
        words = set(value.lower().split())
        if len(words) < 2:
            raise ValidationError('В описании должно быть более 2-ух слов.')
        for i in params:
            if i in words:
                return
        raise ValidationError(f'В описании должны быть слова {", ".join(params)}.')
    return validate
