from django.core.exceptions import ValidationError


def validate_dot(value):
    if '.' in value:
        raise ValidationError('\'.\' is present in the value.')


def validate_owner_todos_count(owner):
    if owner.todo_set.count() > 2:
        raise ValidationError(f"{owner} cannot have more than 2 todos")
