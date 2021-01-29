# @Stocpoolt

# cajero-backend
# cajero-frontend
Contiene indicaciones de cómo se elaboró paso a paso.

# ------------------------------------

# 1.
pip install fastapi
pip install uvicorn
pip install pydantic
pip install SQLAlchemy
pip install psycopg2

Instalar cualquier otro paquete en caso de ser requerido.

# 2.
Crear y modificar:
	-cajero-backend
		__init__.py
		main.py
		-db
			__init__.py
			user_db.py
			transaction_db.py
		-models
			__init__.py
			user_models.py
			transaction_models.py

# 3.
Probar las funcionalidades del main.py en Postman
• Para probar el api en Postman
• (En backend)
		uvicorn main:api --reload

o en Documentación generada por FastAPI
	http://127.0.0.1:8000/docs#/
	http://127.0.0.1:8000/redoc/

# 4.
Crear y modificar:
	-cajero-backend
		Procfile
		requirements.txt

Actualizar repositorio GitHub
Desplegar en Heroku
Probar en Postman con la URL de Heroku
• Para probar el api en Postman
• (En backend)
	uvicorn main:api --reload

# ------------------------------------

# 5.
Instalación de Node.js y NPM

	• Windows	: descargar desde https://nodejs.org/en/ el ejecutable y correrlo, seguir wizard.
	• Linux		: seguir la siguiente guía: https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/

	node --version
	npm --version

# Creación de proyecto en Vue
Instalación de CLI:
• Para poder crear proyectos en Vue
	npm install –g @vue/cli
	vue --version

• Creación del proyecto
• (En la raiz del proyecto)
	vue init webpack cajero-frontend

		Project Name: carejo-frontend
		Project Descripción: una breve descripción
		Author: stocpoolt
		Vue Build: Runtime + Compiler
		Install vue-router? (Y/n): n
		Use ESLint to lint your code? (Y/n): n
		Set up unit test (Y/n): n
		Setup e2e tests with Nightwatch? (Y/n): n
		Should we run…: Yes, use NPM

• Entrar al nuevo folder (cajero-frontend) y ejecutar:
	npm run start
• Dirigirse a la URI http://localhost:808X (Cambiar la "X" por el digito del puerto indicado)

# 6.
-cajero-frontend
    -src
        -components
• Eliminar el archivo HelloWorld.vue
• Editar el archivo App.vue

# 7.
• Ejecutar los siguientes comandos en la raíz del proyecto:
    npm install --save axios
    npm install --save vue-router

# 8.
• En la carpeta src, al mismo nivel de App.vue, crear:
    -src
        router.js

• En carpeta components construir y modificar archivo User.vue y UserBalance.vue:
    -components
        User.vue
        UserBalance.vue

• Modificar archivo App.vue:
    -src
        App.vue
        
# 9.
Para correr la app localmente
# --- AL MISMO TIEMPO ---
    • En la raíz del proyecto de FastAPI (backend):
        uvicorn main:api --reload
    • En la raíz del proyecto de Vue (frontend):
        npm run start
# -----------------------

# 10.
• En la raíz del frontend, crear y modificar archivo server.js:
    -cajero-frontend
        server.js
• Modificar archivo package.json:

# 11.
• Ejecutar el siguiente comando (instalación de servidor Express):
        npm install express serve-static --save
• En la raíz del proyecto, crear un directorio llamado dist:
    -cajero-frontend
        -dist
• Ejecutar en el frontend:
    npm run build
• Como verificaión previa, desplegar el componente localmente:
    node server.js
• Subir los cambios al repositorio de GitHub.

# 12.
• Crear nueva aplicación en Heroku (cajero-frontend) y conectar el repo de GitHub

# 13.
# En backend
• Añadir URI del componente desplegado en Heroku,
    -cajero-backend
        main.py
            origins = [
                "...",
                "...",
                "https://stocpoolt-cajero-frontend.herokuapp.com"
            ]
# 14.
# En frontend
• Modificar las URIs, apuntar la dirección del componente lógico desplegado en Heroku:
    -cajero-frontend
        -src
            -components
                UserBalance.vue
                    axios.get("https://stocpoolt-cajero-backend.herokuapp.com/user/balance/" + this.username)

# 15.
• Actualizar repositorios
• Actualizar los componentes desplegados en Heroku
• Abrir la app desde Heroku

# 16.
# --------------------------------

# Postgres
Es un gestor de base de datos relacionales «opensource», que ha sido usado por mas de 20 años en aplicaciones web, móviles y de análisis.

1. 
# Instalación de PostgreSQL

#   Windows:
        https://www.postgresqltutorial.com/install-postgresql/
#   MacOS:
        https://www.postgresqltutorial.com/install-postgresqlmacos/
        (omitir sección Load the Sample Database)
#   Linux:
        https://www.postgresqltutorial.com/install-postgresql-linux/
        (omitir sección Load the Sample Database)

En el proceso de instalación es importante tener en cuenta:
    • La contraseña ingresada.
    • El puerto asignado.

En Linux, a los datos de contraseña y puerto se le asignan valores por defecto:
Para modificar la contraseña se usan los siguientes comandos:
    you_user:$ sudo –u postgres psql postgres
    postgres=# \password postgres

El puerto por defecto es el 5432

2. 
# pgAdmin
En Linux se debe instalar por aparte:
    https://www.pgadmin.org/download/pgadmin-4-apt/

3. 
# Crear Base de Datos
    MISION-TIC
        Squema: cajerodb (Vacio)
        Squema: Ciclo-lll
            Table: usuario

4. Para ejecutar una query en pgAdmin hacer clic derecho sobre la tabla y seleccionar la herramienta Query Tool y ejecutar el código párrafo a la vez:
    
    4. 1. Insertar un usuario
        INSERT INTO "Ciclo-lll"."Usuario"(id, username, balance)
        VALUES (1, 'Jeisson2020', 9018100);

    4. 2. Modificar el saldo
        UPDATE "Ciclo-lll"."Usuario"
        SET username='Jeisson2021', balance=12050000
        WHERE id=1;

    4. 3. Consultar usuarios
        SELECT id, username, balance
        FROM "Ciclo-lll"."Usuario";

    4. 4. Eliminar usuario
        DELETE FROM "Ciclo-lll"."Usuario"
        WHERE id=1;

# --------------------------------
••• Diapo 16 •••

# Postgres, instalación e integración
Seguir alguna de las siguientes guías de acuerdo a tu sistema
operativo:

Windows: https://www.postgresqltutorial.com/install-postgresql/
MacOS:   https://www.postgresqltutorial.com/install-postgresqlmacos/
		 (omitir sección Load the Sample Database)
Linux:   https://www.postgresqltutorial.com/install-postgresql-linux/
		 (omitir sección Load the Sample Database)

# pgAdmin
En Windows y MacOS se instala por defecto, en Linux se debe instalar por aparte:
	https://www.pgadmin.org/download/pgadmin-4-apt/

• Crear base de datos: MISION-TIC
• Crear tabla: Usuario
• Crear esquema: Ciclo-lll; cajerodb

# 17.
• En db_conection.py, definir:
	-cajero-backend
		-db
			db_conection.py
• Datos de la base de datos Postgres:
	SQLALCHEMY_DATABASE_URL =  "postgresql://postgres:xxx Password xxx@localhost:5432/MISION-TIC"			

• En transaction_db.py, definir:
	-cajero-backend
		-db
			transaction_db.py

# 18.
••• Diapo 18 •••

• En user_models.py, definir:
	-cajero-backend
		-models
			user_models.py

• En transaction_models.py, definir:
	-cajero-backend
		-models
			transaction_models.py

# 19.
• En user_router.py, definir:
	-cajero-backend
		-router
			user_router.py

• En transaction_router.py, definir:
	-cajero-backend
		-router
			transaction_router.py

# 20.
• En main.py, definir:
	-cajero-backend
		main.py

# -------------------------------

# 21. En Query Tool de Postgres
1. Crear usuarios
	INSERT INTO cajerodb.users(username, password, balance)
	VALUES ('camilo24', 'root', 12000);

2. Consultar información de usuario
	SELECT username, password, balance
	FROM cajerodb.users
	WHERE username='camilo24';

3. Consultar transacciones
	SELECT id, username, date, value, actual_balance
	FROM cajerodb.transactions;

# 22. En frontend
• Crear y definir UserAuth.vue; UserTransaction.vue:
	-cajero-frontend
		-src
			-components
				UserAuth.vue
				UserTransaction.vue

• Modificar routers.js:
	-cajero-frontend
		-src
			routers.js

• Modificar App.vue:
	-cajero-frontend
		-src
			App.vue

# ----------------------------------------

# 23.
Luego de aplicar todos los cambios pertinentes correr:
# --- AL MISMO TIEMPO ---
    • En la raíz del proyecto de FastAPI (backend):
        uvicorn main:api --reload
    • En la raíz del proyecto de Vue (frontend):
        npm run start
        
# ----------------------------------------