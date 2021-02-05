from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://rwcyzxxtotyyrh:5047aff5a3814d9fadeea3c12647f5edbcd6a38ce47cabe5c30f8f268991a2a2@ec2-34-230-167-186.compute-1.amazonaws.com:5432/d25v7t3fu2m1dt"
engine                  = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
Base.metadata.schema = "atmdb"