FROM python:3.11

RUN apt-get update -y && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN reflex export --frontend-only --no-zip && mv .web/_static/* /usr/share/nginx/html/ && rm -rf .web

COPY nginx.conf /etc/nginx/conf.d/default.conf

STOPSIGNAL SIGKILL

EXPOSE 8080

CMD [ -d alembic ] && reflex db migrate; \
    service nginx start && \
    exec reflex run --env prod --backend-only