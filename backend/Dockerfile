FROM python:3.10-slim

# Создать пользователя app
RUN addgroup --system app && adduser --system --group app

WORKDIR /app/

# Переменные среды Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

# Установка необходимых системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -sf /root/.local/bin/poetry && \
    poetry config virtualenvs.create false

# Копирование файлов конфигурации Poetry
COPY ./app/pyproject.toml ./app/poetry.lock* /app/

# Установка зависимостей
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --without dev ; fi"

# Копирование кода приложения
COPY ./app /app

# Создание необходимых директорий
RUN mkdir -p /app/files /app/alembic/versions /app/data /app/static

# Делаем скрипты исполняемыми
RUN chmod +x /app/run.sh
RUN if [ -f /app/prestart.sh ]; then chmod +x /app/prestart.sh; fi

ENV PYTHONPATH=/app

# Назначение прав владельца пользователю app
RUN chown -R app:app /app

# Переключение на пользователя app
USER app

# Открытие порта
EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "app.main:app"]