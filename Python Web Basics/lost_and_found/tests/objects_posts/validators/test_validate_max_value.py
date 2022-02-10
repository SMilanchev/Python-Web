from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.validators import validate_max_value


class ValidateMaxValueTests(TestCase):
    def test_ValueIsGreaterThanMax_ExpectToRaise(self):
        value = 5
        validator = validate_max_value(value - 1)
        with self.assertRaises(ValidationError) as e:
            validator(value)
        self.assertIsNotNone(e.exception)

    def test_ValueIsLesserThanMax_ExpectToDoNothing(self):
        value = 5
        validator = validate_max_value(value + 1)
        validator(value)

    def test_ValueIsEqualThanMax_ExpectToDoNothing(self):
        value = 5
        validator = validate_max_value
        validator(value)
