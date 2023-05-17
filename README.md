# blog-sumdu.edu
Solonina Stanislav IH.m-26

## Installation
1. Ensure Python is installed. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

2. Clone the repository:
git clone https://github.com/StanislavSol60/blog-sumdu.edu.git

3. Navigate to the project directory:
cd flask-project

4. Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate

5. Install the required dependencies:
pip install -r requirements.txt

6. Install SQLite (if not already installed):
- For Windows users, download the precompiled binaries from the SQLite website: [SQLite Download](https://www.sqlite.org/download.html)
- For macOS and Linux users, SQLite is typically pre-installed.

7. Configure the environment variables:
- Create a `.flaskenv` file in the project root directory.
- Add the required environment variables from `sample.flaskenv` with yours values, such as:
  ```
  FLASK_APP=app.py
  FLASK_ENV=1
  DATABASE_URL=sqlite:///database.db
  ```

8. Start the development server:
flask run

9. Access the application in your web browser at `http://localhost:5000`.


## Email Testing with Mailtrap
This project uses Mailtrap, a fake SMTP server for email testing. It allows you to intercept and view email messages sent from your application without actually sending them to real recipients.

To use Mailtrap for email testing:
1. Create an account at [Mailtrap](https://mailtrap.io/) if you don't have one.
2. Obtain your Mailtrap SMTP server credentials: `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_USE_TLS`, `MAIL_USE_SSL`.
3. Update the `.flaskenv` file with the Mailtrap credentials.

Now, when your application sends emails, they will be captured by Mailtrap and can be viewed in the Mailtrap inbox associated with your account.