from functools import wraps
from django.core.exceptions import ValidationError
from string import punctuation


def item_text_validator(*params):
    @wraps(item_text_validator)
    def validate(value):
        value = value.translate(str.maketrans('', '', punctuation))
        words = set(value.lower().split())
        must_be = set(params)
        if len(words) < 2:
            raise ValidationError('В описании должно быть более 2-ух слов.')
        diff = must_be - words
        if len(diff) == len(params):
            raise ValidationError(f'В описании должны быть слова {", ".join(params)}.')
    return validate
