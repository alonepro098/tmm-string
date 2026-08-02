from env import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

BASE = declarative_base()


def start() -> scoped_session:
    if not DATABASE_URL:
        return None
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)
        return scoped_session(sessionmaker(bind=engine, autoflush=False))
    except Exception as e:
        print(f"Database connection error: {e}")
        return None


SESSION = start()
