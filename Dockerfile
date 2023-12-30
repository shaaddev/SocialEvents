FROM python:3.9

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT [ "python3" ]
CMD ["manage.py","runserver","0.0.0.0:8000"]