# Usa la imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY talana_kombat.py talana_kombat.py
COPY test_talana_kombat.py test_talana_kombat.py

# Instala las dependencias

# Comando para ejecutar los tests
CMD ["python", "-m", "unittest", "discover"]
