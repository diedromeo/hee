FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache nginx

WORKDIR /app

COPY Pipfile /app/
COPY Pipfile.lock /app/

RUN pip install --upgrade pipenv
RUN pipenv install --system
COPY start.sh /app/
COPY nginx.conf /etc/nginx/
COPY ./ctf /app/ctf
RUN ["chmod", "+x", "/app/start.sh"]

CMD ["sh", "/app/start.sh"]