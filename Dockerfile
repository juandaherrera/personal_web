FROM python:3.11

RUN apt-get update -y && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

RUN pip install uv

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

# Use the system Python environment
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

RUN uv sync

# TODO(@juandaherrera): Remove what is not needed
COPY . .

ARG BACKEND_PORT=8080

RUN reflex export --frontend-only --no-zip && mv .web/_static/* /usr/share/nginx/html/ && rm -rf .web

COPY nginx.conf /etc/nginx/conf.d/default.conf

STOPSIGNAL SIGKILL

EXPOSE 8080

CMD [ -d alembic ] && reflex db migrate; \
    service nginx start && \
    exec reflex run --env prod --backend-only