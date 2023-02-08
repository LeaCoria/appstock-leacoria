# App Stock
Esta aplicación es un simulador de stock, donde el usuario puede registrarse y adquirir productos que estén disponibles.

La aplicación está desplegada en este [enlace](https://appstock-leacoria.herokuapp.com/).


**Este proyecto está creado con Flask**.

***

## Dependencias necesarias  
* [Python](https://www.python.org/)
    * Verifique que su equipo tenga instalado python. Abra una terminal y ejecute el siguiente código:  
    ```
    python --version
    ```
* [PIP](https://pypi.org/project/pip/)
    * Ejecute el siguiente código en una ventana de comandos:
    ```
    sudo apt install python3-pip
    ```
    * Si está utilizando Windows, debe reinstalar Python y seleccionar el apartado "Modify", donde podrá seleccionar la instalación de pip.  


* [PostgreSQL](https://www.postgresql.org/)  
    * Si está trabajando en Linux o Mac, ejecute los siguientes comandos
    ```
    sudo apt-get instal postgresql postgresql-contrib
    ```  
    Cuando finalice la instalación, inserte el usuario (que por defecto es 'postgres') e inicie la base de datos ingresando el siguiente comando:
    ```
    sudo -u postgres psql
    ```  
    La terminal le indicará que está dentro de la base de datos de postgres. Posteriormente cree una contraseña para el usuario 'postgres' ingresando lo siguiente:
    ```
    alter user postgres with password '(INGRESE SU CONTRASEÑA)';
    ```  
    La consola le mostrará un mensaje 'ALTER ROLE', indicando que ya ingresó exitosamente su contraseña.  
    Salga de la base de datos ejecutando:
    ```
    \q
    ```  
***
## Creación de base de datos  
Descargue e instale el gestor de base de datos [DBeaver](https://dbeaver.io/).


Abra la aplicación y seleccione 'nueva conexión'. Seleccione 'PostgreSQL' y haga click en 'Siguiente'.

Ingrese los siguientes valores:
* Host: localhost
* Port: 5432
* Database: postgres
* Nombre de usuario: postgres
* Contraseña: (ingrese la contraseña que creó cuando instaló PostgreSQL).


Haga una prueba de conexión y en caso de que la misma sea exitosa, finalice la conexión. Caso contrario, revise que los valores de database, user y password estén correctamente ingresados.


Una vez conectada la base de datos con el gestor DBeaver, ingrese a la misma y cree una nueva base de datos para ejecutar el código de la aplicación. Preferentemente creela con el nombre 'app_stock'.
***  
## Clonación de repositorio   
Cree una carpeta donde ubicará el proyecto. Abra una terminal en dicha dirección y ejecute el siguiente código:  
```
git clone git@github.com:LeaCoria/App_Stock.git
```  
***  
## Instalación de librerías  
Una vez clonado el código, diríjase a la carpeta raíz del proyecto y abra una terminal. Ejecute los siguientes comandos:  
```
pip3 install pipenv
```  
Cree un entorno virtual:
```
pipenv shell
```  
Una vez dentro, ejecute el siguiente comando que se encargará de instalar las librerías necesarias:
```
pipenv install --ignore-pipfile
```  
***  
## Ingreso de credenciales  
En el directorio raíz del código, cree un archivo que se llame '.env'.


En él ingrese lo siguiente:
```
DB_HOST = localhost
DB_PORT = 5432
DB_USER = postgres
DB_PASSWORD = (su password ingresada para la base de datos)
DB_NAME = (el nombre que le dió a la base de datos)
```  
Guarde los cambios.
## Ejectar la aplicación  
Abra una terminal en la carpeta raíz y dentro del entorno virtual pipenv ejecute:
```
python3 ./app.py
```