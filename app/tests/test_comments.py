import unittest
from unittest import mock
from flask import url_for
from flask_testing import TestCase
from werkzeug.security import generate_password_hash

from app import create_app, db
from app.models.posts import Post
from app.models.users import User
from app.models.comments import Comment


class CommentsTestCase(TestCase):
    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        db.create_all()
        # Create a test user
        self.user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
        db.session.add(self.user)
        db.session.commit()

        # Create a test post
        self.post = Post(title='Test Post', content='Lorem ipsum dolor sit amet', author_id=self.user.id)
        db.session.add(self.post)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @mock.patch('app.routers.users.login')
    @mock.patch('flask_login.utils._get_user')
    def test_add_comment(self, mock_get_user, mock_login):
        mock_login.return_value = None  # Mock the login function
        mock_get_user.return_value = self.user  # Mock the current_user object

        with self.client as client:
            # Perform a request to add a comment
            response = client.post(url_for('comments.add_comment', id=self.post.id), data={
                'content': 'This is a test comment'
            })

            # Assert that the user is redirected to the post route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, ('/{}'.format(self.post.id)))

            # Assert that the comment was added successfully
            self.assertEqual(Comment.query.count(), 1)
            self.assertEqual(len(self.post.comments), 1)
            self.assertEqual(self.post.comments[0].content, 'This is a test comment')

    def test_add_comment_without_login(self):
        with self.client as client:
            # Perform a request to add a comment without logging in
            client.post(url_for('comments.add_comment', id=self.post.id), data={
                'content': 'This is a test comment'
            })

            # Assert that the comment was not added
            self.assertEqual(Comment.query.count(), 0)
            self.assertEqual(len(self.post.comments), 0)


if __name__ == '__main__':
    unittest.main()
