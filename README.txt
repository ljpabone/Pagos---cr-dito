Despliegue en Render:

1. Subir este ZIP como nuevo repositorio.
2. En Render, crear nuevo servicio web.
3. Configurar:
   - Runtime: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app

La aplicación se desplegará en Flask mostrando index.html.
