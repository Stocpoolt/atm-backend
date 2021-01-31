from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creando Motor y Conexion con la Base de Datos
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:EYKjuk83@localhost:5432/MISION-TIC"
engine                  = create_engine(SQLALCHEMY_DATABASE_URL)

#Creacion de la Sesion
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# En get_db inyectamos la dependencia SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creando Base para la creacion de los modelos
Base = declarative_base()

# en la base de datos
Base.metadata.schema = "cajerodb"
