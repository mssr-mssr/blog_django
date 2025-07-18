# 1. Imagen base de Python
FROM python:3.13

# 2.Crear el directorio de trabajo
WORKDIR /app

# 3.Copiar los archivos del proyecto
COPY . /app

# 4. Instalar las dependencias
#Instalar netcat

RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 4.5 Dar permisos al script de entrada
RUN chmod +x entrypoint.sh

# 5. Exponer el puerto 
EXPOSE 8000

# 6. Usar el entrypoint para esperar y arrancar
ENTRYPOINT [ "/app/entrypoint.sh" ]
