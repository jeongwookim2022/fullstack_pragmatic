from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    # secret_key 갖고 오면 양 옆에 불필요한 공백이 있음.
    # secret = secret.rstrip().lstrip()
    file.close()

    return secret


env = environ.Env(
    DEBUG=(bool, False)
)

#Reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# 처음에는 env 파일에서 갖고 오도록 서절을 했음 ------- (1)
# Docker secrets를 사용하여 secret에서 갖고 오도록 다시 설정. -------- (2)
# (1)
# SECRET_KEY = env('SECRET_KEY')
# (2)
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        # 'PASSWORD': 'password1234',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'HOST': 'mariadb', # mariadb container 이름
        'PORT': '3306',
    }
}