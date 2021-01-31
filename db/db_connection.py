from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creando Motor y Conexion con la Base de Datos
SQLALCHEMY_DATABASE_URL = "postgresql://pfmgsthduacgul:33f4730a1f02534aa6430ab33ba98bcdf92ca37d9fd8a2a353621d2834510941@ec2-34-232-24-202.compute-1.amazonaws.com:5432/d28bq97v9om3l5"
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
Base.metadata.schema = "atmdb"
