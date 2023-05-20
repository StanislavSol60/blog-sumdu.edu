import unittest
from flask_testing import TestCase
from werkzeug.security import generate_password_hash
from flask import url_for
from app import create_app, db
from app.models.users import User
from app.models.posts import Post
from app.models.comments import Comment



class PostsTestCase(TestCase):
    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        db.create_all()
        # Create a test user
        self.user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')

    def test_my_posts(self):
        with self.client as client:
            # Log in a user
            client.post('/login', data={
                'email': 'test@example.com',
                'password': 'testpassword',
                'remember': False
            })

            response = self.client.get('/posts')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def test_post(self):
        # Create a test post
        post = Post(title='Test Post', content='Lorem ipsum dolor sit amet', author_id=self.user.id)
        db.session.add(post)
        db.session.commit()

        response = self.client.get(f'/{post.id}')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('post.html')

    def test_create(self):
        with self.client as client:
            # Perform a login request with valid credentials
            client.post(url_for('users.login'), data={
                'email': 'test@example.com',
                'password': 'testpassword',
            })

            # Perform a request to add a comment
            response = client.post(url_for('posts.create'), data={
                'title': 'Test Post', 'content': 'Lorem ipsum dolor sit amet', 'author_id': self.user.id
            })

            # Assert that the user is redirected to the posts route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/posts')

            posts = list(Post.query.all())

            # Assert that the post was added successfully
            self.assertEqual(len(posts), 1)
            self.assertEqual(posts[0].title, 'Test Post')
            self.assertEqual(posts[0].content, 'Lorem ipsum dolor sit amet')
            self.assertEqual(posts[0].author_id, self.user.id)

    def test_edit(self):
        with self.client as client:
            # Perform a login request with valid credentials
            client.post(url_for('users.login'), data={
                'email': 'test@example.com',
                'password': 'testpassword',
            })

            # Create a test post
            post = Post(title='Test Post', content='Lorem ipsum dolor sit amet', author_id=self.user.id)
            db.session.add(post)
            db.session.commit()

            # Perform a request to edit a post
            client.post(url_for('posts.edit', id=post.id), data={
                 'title': 'New Test Post Title', 'content': 'New Test Post Content'
            })

            updated_post = Post.query.get(post.id)

            # Assert that the post was updated successfully
            self.assertEqual(updated_post.title, 'New Test Post Title')
            self.assertEqual(updated_post.content, 'New Test Post Content')

    def test_delete_post(self):
        with self.client as client:
            # Perform a login request with valid credentials
            client.post(url_for('users.login'), data={
                'email': 'test@example.com',
                'password': 'testpassword',
            })

            post = Post(title='Test Post', content='Lorem ipsum dolor sit amet', author_id=self.user.id)
            db.session.add(post)
            db.session.commit()

            # Perform a request to delete the post
            response = client.get(url_for('posts.delete', id=post.id))

            # Assert that the user is redirected to the posts route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/posts')

            # Assert that the post was deleted
            deleted_post = Post.query.get(post.id)
            self.assertIsNone(deleted_post)
            deleted_comments = Comment.query.filter_by(post_id=post.id).all()
            self.assertEqual(len(deleted_comments), 0)

            # Assert that the success message is flashed
            with client.session_transaction() as session:
                flash_messages = session['_flashes']
                self.assertEqual(len(flash_messages), 1)
                self.assertEqual(flash_messages[0][1], '"Test Post" was successfully deleted!')


if __name__ == '__main__':
    unittest.main()
