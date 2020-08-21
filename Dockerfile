FROM python:3
ENV PYTHONBUFFERED 1

RUN mkdir /portfolio
WORKDIR /portfolio

COPY ./requirements.txt /portfolio/requirements.txt
RUN pip install -r requirements.txt

COPY ./portfolio /portfolio

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000

#CMD python manage.py runserver 0.0.0.0:8000 , says wrong port address
