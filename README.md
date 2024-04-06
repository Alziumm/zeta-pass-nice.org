# zeta-pass-nice.org - PRODUCTION

## Description:

This is an extremely easy Django application to use.

## Features:

- Feature 1: Simplified page display.
- Feature 2: Contact form with Telegram endpoint.

## Installation:

1. Clone the repository: `git clone https://github.com/votre-repo.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Add a .env file to the root of the project and include the variables:
    * PRODUCTION=1
    * SECRET_KEY="insert_encrypt_key_here"
    * TELEGRAM_ENDPOINT = "https://api.telegram.org/botXXXXXXXXX:xxxxxxxxxxxxxx/sendMessage?chat_id=xxxxxxxx&text="
4. Configure the database: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Access the application in your browser: `http://127.0.0.1:8000`