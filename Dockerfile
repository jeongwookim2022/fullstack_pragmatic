#venv
# - 처음에 가상환경을 만들고 그 안에 관련 package들을 넣었음.
# - pip list를 terminal에 치면 지금까지 가상환경에 설치한 package들을 볼 수 있음.
#
# 왜 이 얘기를 하냐?
# --> 새로 만들 django container에서도 위의 package들을 설치해야 한다!
# 그래서 어떤 Library를 설치했는지를 알려줘야 한다.
# 어떻게?
# --> pip freeze > requirements.txt 그리고 마찬가지로 이것도 git에 commit한다.
#      그리고 이미 github에 소스 코드들을 올렸는데 requirements.txt가 추가가 되었     으므로 git push 명령어를 통해 github에 업로드 가능해짐.


# 이것을 base로 하여 Image를 갖고 옴
FROM python:3.9.0


# 실제 Linux OS에서처럼 DIR 설정
WORKDIR /home/


#의미 없음
RUN echo "teeeest2222aaaadddadf22"

# github에 올린 소스 코드를 갖고 온다.
# --> 그러면 갖고 온 소스 코드가 Image 안에 들어가게 된다.
RUN git clone https://github.com/jeongwookim2022/pragmatic.git


# git clone명령어로 소스 코드를 갖고 왔기 때문에, Linux OS의 home 하위에
# pragmatic이라는 폴더가 생김. 그래서 경로를 다시 설정해준다.
WORKDIR /home/pragmatic/


# 이 Image 내에서도 개발 때 사용한 라이브러리를 설치해야 한다
# -> requirement.txt를 사용하여 알려준다.
RUN pip install -r requirements.txt


##################################################################
RUN pip install gunicorn
##################################################################


RUN pip install mysqlclient


##################################################################
# 이렇게 작성하면 Image 내에서 "SECRET_KEY~~"를 가진 .env 파일이 생성됨.
# Docker Secret 만들고 이를 임시의 SECRET_KEY 주석처리 함.
# RUN echo "SECRET_KEY=지움" > .env
##################################################################


# migrate: DB와 연동시켜줌
# 아직 marid DB같은 외부 DB와 연동시키진 않았지만,
# Linux 내부에 생긴 sqlite DB와 연동을 시켜줌.
# (local에서 했던 것과 동일한 것을 가상 서버에서 진행중인 것임)

# RUN python manage.py migrate (mariaDB 사용하면서 뺌)


# Django container에 있는 static contents를 NGINX container에
# 동기화시키기 위해 static contents를 한 곳에 모으기 위한 명렁어 추가.

# 추가적으로, secret을 사용하면 Image를 만드는 도중에는 제공 안 됨. 즉, container가 만들어진 후에 제공 됨.
# 그러므로 이 명령어를 뒤로 몰아준다.
# RUN python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy


# EXPOSE: django container의 port를 외부에 노출시켜줌.
# django의 port와 외부(가상서버)의 port와 연결이 가능하도록, django의 port를 외부에 노출시켜줌.
EXPOSE 8000


# (1)만 작성하고 돌리면 안됨
# 왜?
# --> 개발 초반에 SECRET_KEY를 .env 파일에 옮긴후 .gitignore로 감췄음.
#     그래서 github에는 SECRET_KEY에 대한 내용이 없음. 그래서 django 안 돌아감.
# 그럼 어떻게 해?
# --> 여기서 임시로 SECRET_KEY를 만든다


# (1)
# 또한, manage.py runserver는 개발 단계에서 테스트용으로 사용하는 것이므로.
# 이 명령어를 바꿔줘야 할 필요가 있다. --> (2)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# (2)
# gunicorn을 사용하여 manage.py gunicorn을 바꾼다.
# 그러므로 Image가 container화 되어서 실행될 때 쓰이는 명령어를 다음과 같이 바꿈.
# -- noinput: staic을 collec할 때 input 묻지 말고 알아서 해라.
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
