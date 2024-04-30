from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

from app.env import Env

_database_url = URL.create(
    drivername="mysql+mysqldb",
    username=Env.DATABASE_USER,
    password=Env.DATABASE_PASSWORD,
    host=Env.DATABASE_HOST,
    port=int(Env.DATABASE_PORT),
    database=Env.DATABASE_NAME,
)

engine = create_engine(
    _database_url,
    echo=True,
    pool_size=100,
    max_overflow=0,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
