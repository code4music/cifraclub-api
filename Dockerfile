FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install \
  pylint \
  pytest \
  pytest-cov

COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python3", "api.py"]
