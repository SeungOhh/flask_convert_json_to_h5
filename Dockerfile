FROM python:3.7

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask_cors
RUN pip install tensorflowjs==2.0.1
RUN pip install scipy==1.4.1
RUN pip install tensorflow==2.3.0
RUN pip install gunicorn==19.9.0

WORKDIR /app
COPY . /app

EXPOSE 5050
CMD python ./index.py