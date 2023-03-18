# Configuración del archivo de configuración

El archivo de configuración proporcionado se utiliza para configurar el almacenamiento y el nombre del contenedor de Docker, así como los nombres de las bases de datos utilizadas para entornos de desarrollo y prueba.

## Uso del archivo de configuración

El archivo de configuración se divide en dos secciones: `[general]` y `[databases_names]`.

### `[general]`:

La sección `[general]` contiene dos claves:

- `docker_storage_dir`: especifica la ruta donde se almacenarán las copias de seguridad de las bases de datos en el contenedor Docker.
- `container_name`: especifica el nombre del contenedor Docker utilizado para la base de datos.

Para modificar estas configuraciones, simplemente cambie los valores que se proporcionan a continuación de cada clave.

### `[databases_names]`:

La sección `[databases_names]` contiene los nombres de las bases de datos donde se restauraran las bases de datos.

Para agregar nuevas bases de datos, simplemente agregue una nueva línea en la sección `[databases_names]`, donde la clave es el nombre del entorno (por ejemplo, "producción") y el valor es el nombre de la base de datos (por ejemplo, "sample_production").

Para cambiar los nombres de las bases de datos existentes, simplemente modifique el valor correspondiente a la clave correspondiente.

**Nota:** Se puede agregar tantas bases de datos como desee, pero tenga en cuenta que a mayor cantidad de bases de datos, mayor será el tiempo de ejecución.

