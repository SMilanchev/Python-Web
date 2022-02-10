from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.models import Object


class ObjectTests(TestCase):
    valid_name = 'Peshko'
    valid_image = 'https://image.com'
    valid_width = 500
    valid_height = 200
    valid_weight = 400

    def test_WhenWidthIsLesserThan3_ExpectRaise(self):
        width = 2

        p = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        with self.assertRaises(ValidationError) as exc:
            p.full_clean()
            p.save()

        self.assertIsNotNone(exc.exception)

    def test_WhenWidthIsEqualTo3_ExpectSuccess(self):
        width = 3

        p = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        p.full_clean()
        p.save()


    def test_WhenWidthIsGreaterThan600_ExpectRaise(self):
        width = 601

        p = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        with self.assertRaises(ValidationError) as exc:
            p.full_clean()
            p.save()

        self.assertIsNotNone(exc.exception)

    def test_WhenWidthIsEqualTo600_ExpectSuccess(self):
        width = 600

        p = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        p.full_clean()
        p.save()

    def test_WhenWidthIsBetween3And600_ExpectSuccess(self):

        p = Object(
            name=self.valid_name,
            image=self.valid_image,
            width=self.valid_width,
            height=self.valid_height,
            weight=self.valid_weight,
        )

        p.full_clean()
        p.save()
