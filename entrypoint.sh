#!/bin/sh

echo "Esperando a que la base de datos esté lista..."

#Proceso de espera

while ! nc -z db 5432; do 
    sleep 1
done

echo "Base de datos disponible, arrancando Django web"

#levantar parte web (runserver)
python manage.py runserver 0.0.0.0:8000
