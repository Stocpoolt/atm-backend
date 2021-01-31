# Comandos en Postgres
(Atender a las comillas, algunas son sencillas y otras deben ser dobles)

1. Consultar información:
	select *																					| Seleccionar todo
	from public. "Usuario"														| De la tabla "Usuarios"

2. Insertar elementos
	insert into public. "Usuarios" (nombre, correo)   | Insertar en tabla "Usuarios" los espacios (nombre y correo)
	values ('Carlos Andres', 'example@email.com')		  | Los valores de nombre y correo
	
3. Actualizar información (Corregir)
	update public. "Usuarios"													| De la tabla "Usuarios"
	set correo = "example@yahoo.com"									| Colocar el nuevo correo "example@email.com"
	where id = 2																			| A la fila con id = 2
	
4. Eliminar registros
	delete public. "Usuarios"													| De la tabla "Usuarios"
	where id = 3																			| Eliminar los datos de la fila con id = 3

#---------------------------------------------------------------------------------------------------

# Postgres en Heroku

1. Instalar:
    $ sudo snap install --classic heroku

2. Loguearse:
    $ heroku login

3. En la raiz del proyecto:
    $ git init
    $ heroku git:remote -a stocpoolt-formulario

    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master

4. En caso de no hacer push por no tener tipo:
    4. 1. Correr en la raiz:
        heroku buildpacks:set heroku/php
    4. 2. Crear y modificar
        index.php
            <?php include_once("index.html"); ?>
        composer.json
            {

            }

#---------------------------------------------------------------------------------------------------

# SQLite desde Django
# Para ejecutar cambios al modelo correr en la raíz del proyecto:
	~$ python manage.py makemigrations
	~$ python manage.py migrate

- En la raiz del proyecto
	python manage.py shell
	>>> from gestionPedidos.models import Articulos   | from Carpeta de la app.models import Tabla

1. Agregar elementos
	a. art=Articulos(nombre="Mesa", seccion="Decoración", precio=90) | Variable=Tabla(Columna="Valor", ...)
	   art.save()
	
	b. art=Articulos.objects.create(nombre="Mesa", seccion="Decoración", precio=90)
	
2. Modificar elementos
	art.precio=95                                     | Nombre variable a cambiar.Columna=Nuevo valor
	art.save()
	
3. Eliminar elementos
	art1=Articulos.objects.get(id=1)									| Nueva variable=Tabla.objects.get(id= ...)
	art5.delete()
	
4. Consultar
	a. Lista=Articulos.objects.all()
		 Lista
		 
	b. Articulos.objects.filter(seccion="Deportes")		| Nombre tabla.objects,filter(filtro1="",filtro2="", ...)
	
	c. Articulos.objects.filter(seccion="Deportes", precio__gte=100)					| __gte = Mayor que
	d. Articulos.objects.filter(seccion="Deportes", precio__lte=100)					| __lte = Menor que
	e. Articulos.objects.filter(seccion="Deportes", precio__range=(100,150)		| __range(Entre el rango)
	f. Articulos.objects.filter(precio__gte=100).order_by("precio")						| En orden ascendente numérico o alfabético
	f. Articulos.objects.filter(precio__gte=100).order_by("-precio")					| En orden descendente numérico o alfabético