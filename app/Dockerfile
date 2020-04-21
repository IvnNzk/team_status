FROM python:3.7-slim
MAINTAINER Ivan Oschepkov <ivan@oschepkov.ru>

ADD . /opt/
WORKDIR /opt/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
