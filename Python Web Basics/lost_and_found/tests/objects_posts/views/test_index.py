from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse


class IndexTests(TestCase):
    @patch('lost_and_found.objects_posts.models.Post.objects')
    def test_example(self, mocked_object):
        mocked_object.all.return_value = ['pesho']
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        posts = response.context['posts']
        pass