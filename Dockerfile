FROM python:3.8.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip --use-feature=2020-resolver install -r requirements.txt
COPY . /code/
RUN chmod +x /code/docker-entrypoint.sh
