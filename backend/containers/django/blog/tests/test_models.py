from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker

from blog.models import Post
from blog.models import PostBody
from blog.models import Profile


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testman", password="testpass")
        cls.profile = Profile.objects.create(user=cls.user)
        cls.body = baker.make("blog.PostBody", text=" Test", post__title="Test title")
        print(f"Title : {cls.body.post.title}")
        print(cls.body.text)

    def create_post(
        self,
        title="test title",
        text="test",
    ):
        post = Post.objects.create(title=title, author=self.profile)
        body = PostBody.objects.create(post=post, text=text)
        return post

    def test_post_creation(self):
        w = self.create_post()
        self.assertTrue(isinstance(w, Post))

    def test_is_profile_instance_of_profile_model(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_post_body(self):
        self.assertTrue(isinstance(self.body, PostBody))
