import unittest
from flask_login import current_user
from flask_testing import TestCase
from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models.users import User


class UsersTestCase(TestCase):

    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login(self):
        with self.client as client:
            # Create a test user
            user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
            db.session.add(user)
            db.session.commit()

            # Send a POST request to the login route
            response = client.post('/login', data={
                'email': 'test@example.com',
                'password': 'testpassword',
                'remember': False
            })

            # Assert that the user is authenticated
            self.assertEqual(current_user.is_authenticated, True)

            # Assert that the user is redirected to the posts route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/posts')

    def test_login_failed(self):
        with self.client as client:
            # Create a test user
            user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
            db.session.add(user)
            db.session.commit()

            # Send a POST request to the login route
            client.post('/login', data={
                'email': 'test@example.com',
                'password': 'newtestpassword',
                'remember': False
            })

            # Assert that the user receives a message
            self.assert_message_flashed('Invalid email or password')
            # Assert that the user is authenticated
            self.assertEqual(current_user.is_authenticated, False)

    def test_signup(self):
        with self.client as client:
            # Send a POST request to the signup route
            response = client.post('/signup', data={
                'email': 'test@example.com',
                'name': 'Test User',
                'password': 'testpassword',
                'confirm_password': 'testpassword'
            })

            # Assert that the user is redirected to the login route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/login')

    def test_signup_existing_user(self):
        with self.client as client:
            # Create a test user
            user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
            db.session.add(user)
            db.session.commit()

            # Send a POST request to the signup route
            response = client.post('/signup', data={
                'email': 'test@example.com',
                'name': 'Test User',
                'password': 'testpassword',
                'confirm_password': 'testpassword'
            })

            # Assert that the user receives a message
            self.assert_message_flashed('Email already taken. Please choose another email.')

    def test_profile(self):

        with self.client as client:
            # Create a test user
            user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
            db.session.add(user)
            db.session.commit()

            # Send a POST request to the login route
            client.post('/login', data={
                'email': 'test@example.com',
                'password': 'testpassword',
                'remember': False
            })

            # Assert that the user is authenticated
            self.assertEqual(current_user.is_authenticated, True)

            # Send a POST request to the profile route
            client.post('/profile', data={
                'name': 'Updated Name',
                'email': 'updated@example.com',
                'date_of_birth': '1990-01-01',
                'gender': 'M'
            })

            # Retrieve the updated user from the database
            updated_user = User.query.filter_by(email='updated@example.com').first()

            # Assert that the user's information is updated
            self.assertIsNotNone(updated_user)
            self.assertEqual(updated_user.name, 'Updated Name')
            self.assertEqual(updated_user.date_of_birth.strftime('%Y-%m-%d'), '1990-01-01')
            self.assertEqual(updated_user.gender, 'M')

    def test_logout(self):

        with self.client as client:
            # Create a test user
            user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
            db.session.add(user)
            db.session.commit()

            # Send a POST request to the login route
            response = client.post('/login', data={
                'email': 'test@example.com',
                'password': 'testpassword',
                'remember': False
            })

            # Send a GET request to the logout route
            response = self.client.get('/logout')

            # Assert that the user is not authenticated
            self.assertEqual(current_user.is_authenticated, False)

            # Assert that the user is redirected to the login route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/login')

    def test_forgot_password(self):

        with self.client as client:
            # Create a test user
            user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
            db.session.add(user)
            db.session.commit()

            # Send a POST request to the forgot_password route
            response = client.post('/forgot_password', data={
                'email': 'test@example.com',
            })

            # Assert the email content or perform additional assertions if needed

            # Assert that the user is redirected to the login route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/login')

    def test_reset_password(self):

        with self.client as client:
            # Create a test user
            user = User(email='test@example.com', name='Test User', password=generate_password_hash('testpassword'))
            db.session.add(user)
            db.session.commit()
            token = user.generate_reset_token()
            user.reset_token = token

            # Send a GET request to the reset_password route
            client.get(f'/reset_password/{user.reset_token}')

            # Assert that the user is able to access the password reset form
            self.assert_template_used('reset_password.html')

            # Send a POST request to the reset_password route with a new password
            response = self.client.post(f'/reset_password/{user.reset_token}', data={
                'password': 'newpassword',
                'confirm_password': 'newpassword'
            })

            # Assert that the user receives a success message
            self.assert_message_flashed('Your password has been reset.', 'success')

            # Assert that the user is redirected to the login route
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/login')


if __name__ == '__main__':
    unittest.main()
