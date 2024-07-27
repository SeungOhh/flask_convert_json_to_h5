FROM python:3.7


RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask_cors
RUN pip install tensorflowjs==2.0.1
RUN pip install scipy==1.4.1
RUN pip install tensorflow==2.3.0
RUN pip install gunicorn==19.9.0
RUN pip install pyopenssl


WORKDIR /app
COPY . /app


EXPOSE 5000
# CMD python ./index.py
# CMD gunicorn -w 2 -b 0.0.0.0:443 index:app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "index:app"]