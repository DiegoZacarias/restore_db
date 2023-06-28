## Instalación del script

1. Clona el proyecto de GitHub en tu ordenador usando el comando `git clone`:
git clone https://github.com/DiegoZacarias/restore_db

2. Dirígete a la carpeta donde se encuentra el script usando el comando `cd`:
cd proyecto

3. Crear carpeta dependencies:
mkdir dependencies

4. Instala las librerías necesarias para el script usando el archivo `requirements.txt`, dependiendo si usas python3 o python2:
pip install -r requirements.txt --target=dependencies
pip3 install -r requirements.txt --target=dependencies

Este comando instalará todas las librerías necesarias para que el script funcione correctamente en tu ordenador.
Importante: Estas librerias solo estaran instaladas dentro del proyecto, es decir, que no se podran utilizar fuera de la carpeta del proyecto 

## Configuración del archivo de configuración

El archivo de configuración proporcionado se utiliza para configurar el almacenamiento y el nombre del contenedor de Docker, así como los nombres de las bases de datos utilizadas para entornos de desarrollo y prueba.

### Uso del archivo de configuración

El archivo de configuración se divide en dos secciones: `[general]` y `[databases_names]`.

- `[general]`: contiene dos claves: `docker_storage_dir` y `container_name`. Para modificar estas configuraciones, simplemente cambie los valores que se proporcionan a continuación de cada clave.

- `[databases_names]`: contiene los nombres de las bases de datos donde se restauraran las bases de datos. Para agregar nuevas bases de datos, simplemente agregue una nueva línea en la sección `[databases_names]`, donde la clave es el nombre del entorno y el valor es el nombre de la base de datos. Para cambiar los nombres de las bases de datos existentes, simplemente modifique el valor correspondiente a la clave correspondiente.


**Nota:** Se puede agregar tantas bases de datos como desee.

5. Ejecuta el script 'main.py' y espera unos minutos a que termine el proceso

## Compatibilidad y Pruebas

Este proyecto ha sido probado y es compatible con los siguientes sistemas operativos:

- Windows
- Mac/Linux
