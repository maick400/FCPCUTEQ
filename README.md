## Codigos de ejecución
***
## 1. Clonar repositoro

inicializar
```console 
git init  
```

configurar usuario y email
```console 
git config --global user.name "username"
```

```console 
git config --global user.email "email"
```

```console 
git remote add origin https://github.com/maick400/FCPCUTEQ.git
```

```console 
git pull origin main
```


## 2. Clonar repositoro

Crear entorno virtual.

windows 
1. Crear entorno virtual
***
```console 
python -m venv venv
```

2. Activar entorno virtual

```console 
./venv/Scripts/activate.bat
```

## 3. Instalar dependencias

Crear entorno virtual.

windows 


```console 
pip install -r ./requeriments.txt```
```

## 4. Crear arichivo de configuración

Crear un archivo `.env`dentro de la carpeta raíz, y dentro de ello colocar los parémtros necesario de acuerdo a su equipo: 

```conf
DATABASE_NAME=FCPCUTEQ
DATABASE_USER=postgres
DATABASE_PASSWORD=123456
DATABASE_HOST=localhost
DATABASE_PORT=5432
SECRET_KEY=maick400.
```

## 5. EJecución
Despues de agregado el archivo de configuración, realizar las migraciones este comando es necesario cuando se realiza la primera instalación, o se realiza cualquier cambio al un modelo. 

```console
python ./manage.py makemigrations
```
```console
python ./manage.py migrate
```

Crear super usuario (Solo por vez primera)
```console
python ./manage.py createsuperuser
```

Correr app 
```console
python ./manage.py runserver
```




