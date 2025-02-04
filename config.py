import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwtsecretkey')
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 1 day
    SQLALCHEMY_DATABASE_URI = "mysql://root:First1058@localhost/kmitl_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
