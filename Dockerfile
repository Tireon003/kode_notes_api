FROM python:3.12

RUN mkdir /src

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app app

ENV PYTHONPATH=/src/app

CMD uvicorn main:app --host 0.0.0.0 --port 8000
