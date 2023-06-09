# blog-sumdu.edu
Solonina Stanislav IH.m-26

## Installation
1. Ensure Python is installed. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

2. Clone the repository:
git clone https://github.com/StanislavSol60/blog-sumdu.edu.git

3. Navigate to the project directory

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


# Unit Tests
This project includes unit tests to verify the functionality of various components.
## Running Unit Tests

To run the unit tests, use the following command:

python -m unittest discover -s app/tests/unit
This command will automatically discover and execute all the unit test files located in the `app/tests/unit` directory.
It's recommended to set up a virtual environment and install the required dependencies before running the unit tests.

## Test Coverage

Test coverage measures the percentage of code covered by the unit tests. It helps identify areas of code that are not adequately tested.
To generate a test coverage report, you can use tools like `coverage.py`. Here's an example command:
coverage run -m unittest discover -s app/tests/unit

After running the tests, you can generate a coverage report using the following command:

coverage report
This will display a detailed report showing the coverage percentage for each file.

# Selenium Tests
This project includes Selenium tests to verify the functionality through the web interface.

## Running Selenium Tests
To run the Selenium tests using pytest, execute the following command:

pytest app/tests/selenium
This command will run all the tests located in the `app/tests/selenium` directory.
It's recommended to set up a virtual environment and install the required dependencies before running the selenium tests.
