import dotenv, os
dotenv.load_dotenv()


class Config:
   SECRET_KEY = os.getenv('SECRET_KEY')
   SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 465
   MAIL_USE_SSL = True
   MAIL_USERNAME = os.getenv('EMAIL')
   MAIL_PASSWORD = os.getenv('PASS')