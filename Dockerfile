FROM nikolaik/python-nodejs:python3.7-nodejs16

WORKDIR /code

EXPOSE 8000

COPY .env /code/.env
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
