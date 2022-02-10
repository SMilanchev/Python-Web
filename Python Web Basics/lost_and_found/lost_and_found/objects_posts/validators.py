from django.core.exceptions import ValidationError


def validate_max_value(max_value):
    def internal_validator(value):
        if value > max_value:
            raise ValidationError(f'Value cannot be bigger than {max_value}')

    return internal_validator
