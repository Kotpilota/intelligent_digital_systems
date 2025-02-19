#!/bin/sh

#!/bin/sh

# Path to local package /app
export PYTHONPATH=$PWD # 0
export BACKEND_CORS_ORIGINS=["http://localhost","http://localhost:4200","http://localhost:8001","http://localhost:3000","https://localhost:8001"]
# export DATABASE_URL=postgresql+asyncpg://fastapi_user:fastapi_pwd@localhost:5432/fastapi_db
export DATABASE_URL=sqlite+aiosqlite:///./database.db

# Heroku postgres addon
export SQLALCHEMY_DATABASE_URI=${DATABASE_URL}  # 1

# If there's a prestart.sh script in the /app directory or other path specified, run it before starting
#PRE_START_PATH=${PRE_START_PATH:-/app/prestart.sh}  # 2
PRE_START_PATH=${PRE_START_PATH:-./prestart.sh}  # 2
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else
    echo "There is no script $PRE_START_PATH"
fi

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-80}  # 3
export BACKEND_CORS_ORIGINS=${BACKEND_CORS_ORIGINS}  # 4


# run gunicorn
exec gunicorn --bind $HOST:$PORT "$APP_MODULE" -k uvicorn.workers.UvicornWorker  # 5
