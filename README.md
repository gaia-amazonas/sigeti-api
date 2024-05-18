# sigeti-api
API basada en Django REST Framework para direccionar a usuarios generados distribuidamente en grupos para consultar bases de datos en las plataformas BigQuery y SQL de GCP.


## APT-GET CURLS: Primer paso

Recuerde antes de desplegar esta aplicación, primero hacer los curls para añadir repositorios de paquetes

```curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg```


## Instale los paquetes para Ubuntu 22.04: Segundo paso

Con los repositorios nuevos añadidos, instalar los paquetes contenidos en ```packages.list```.


## Cree y Active un ambiente virtual: Tercer paso

- Con ```python3 -m venv .venv``` cree un ambiente virtual de Python especial para la API.
- Con ```souce .venv/bin/activate``` active el ambiente virtual para desplegar la API.


## Instale los paquetes Python

Con ```pip install -r requirements.txt```


## Inicialice Google CLI para crear conectar la API:  paso

Con ```gcloud init``` conecte el servidor con la Aplicación sigeti-admin-364713 en GCP, siga los pasos y utilice las credenciales (contraseña y correos) de la organización que le dio Gaia Amazonas.


## Autenticación con su usuario de Google organizacional

Con ```gcloud auth login``` autentique su usuario para utilizarlo en la consola del servidor.