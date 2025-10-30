Despliegue en Render:

1. Sube este proyecto a un repositorio en GitHub.
2. En Render, crea un nuevo Web Service.
3. Configura:
   - Runtime: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
4. Render detectará automáticamente app.py y la carpeta templates.
5. La base de datos SQLite se creará automáticamente.
6. Para usar PostgreSQL, cambia la URI en app.py y configura DATABASE_URL en Render.
