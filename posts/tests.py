from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        test_user = User.objects.create_user(
            username='Test user',
            password='abc123'
        )
        test_user.save()

        test_post = Post.objects.create(
            author=test_user,
            title='Blog title',
            body='Blog content'
        )
        test_post.save()
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'Test user')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Blog content')