FROM python:3.10

# create the app user
RUN addgroup --system app && adduser --system --group app

WORKDIR /app/

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -sf /root/.local/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./app/pyproject.toml ./app/poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --without dev ; fi"

# Copy application code
COPY ./app /app

# Create necessary directories
RUN mkdir -p /app/files /app/alembic/versions /app/data /app/static /app/media

# Copy and make entrypoint executable
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

ENV PYTHONPATH=/app

# Give proper ownership to the app user
RUN chown -R app:app /app

# change to the app user
USER app

# Run the entrypoint script and then the app
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "app.main:app"]