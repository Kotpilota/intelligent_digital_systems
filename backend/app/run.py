
import subprocess
import sys, os
from pathlib import Path

# print(str(Path(__file__).resolve().parent / "alembic/versions") )
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///database.db"
os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite+aiosqlite:///./database.db"
os.environ["PYTHONPATH"] = str(Path(__file__).resolve().parent)
os.environ["BACKEND_CORS_ORIGINS"]="http://localhost,http://localhost:80,http://localhost:4200,http://localhost:8001,http://localhost:3000,https://localhost:8001"

if not os.path.exists( str(Path(__file__).resolve().parent / "alembic/versions") ) :
    os.mkdir( str(Path(__file__).resolve().parent / "alembic/versions") )
    print(">>> run.py. Creating versions folder in alembic")

if os.path.exists("./prestart.py") :
    subprocess.run([sys.executable, "./prestart.py"])
else:
    print("There is no script ./prestart.py")




subprocess.run([sys.executable, "./app/main.py"])
