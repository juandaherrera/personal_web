# Stage 1: Construir archivos estáticos con Python
FROM python:3.11 AS builder

WORKDIR /app

# Copia los archivos necesarios para instalar dependencias
COPY requirements.txt .

# Configura el entorno virtual de Python
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente de la aplicación al contenedor
COPY . .

# Genera los archivos estáticos
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Stage 2: Configurar Nginx para servir los archivos estáticos
FROM nginx:alpine

# Copia los archivos estáticos del builder al directorio de Nginx
COPY --from=builder /app/.web/_static /usr/share/nginx/html

# Expone el puerto 80
EXPOSE 80

# Inicia nginx
CMD ["nginx", "-g", "daemon off;"]
