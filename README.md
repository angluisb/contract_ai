# Contract AI

Análisis de contratos legales con inteligencia artificial, desarrollado con Django.

---

## 📖 Descripción

Contract AI es una aplicación web que permite a los usuarios subir contratos legales y hacer preguntas sobre su contenido. Utiliza inteligencia artificial para analizar el documento y brindar respuestas personalizadas mediante un sistema de chat integrado.

Esta herramienta está diseñada para resolver dos grandes problemas:

- La falta de conocimiento legal por parte de los usuarios.
- La escasez de personal legal en pequeñas y medianas empresas (PyMEs).

---

## 🚀 Características principales

- 📄 Análisis automático de contratos subidos por los usuarios.
- 🤖 Chat impulsado por IA para responder dudas específicas sobre el contrato.
- 🔐 Gestión de usuarios y autenticación segura.

---

## 🧰 Tecnologías utilizadas

- Django (backend y sistema de templates)
- Python
- PostgreSQL
- API de Gemini (Google AI)
- HTML y CSS con Django Templates

---

## ⚙️ Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/angluisb/contract_ai.git
   cd contract_ai
2. Crea un entorno virtual:
    
    ```bash
    python -m venv venv
    source venv/bin/activate      # En Unix/macOS
    venv\Scripts\activate         # En Windows
3. Instala las dependencias:
   
   ```bash
   pip install -r requirements.txt
4. Configura las variables de entorno (ver sección .env).
   
5. Ejecuta las migraciones:
   ```bash
   python manage.py migrate

6. Crea un superusuario:
    ```bash
    python manage.py createsuperuser

7. Ejecuta el servidor de desarrollo:
   ``` bash
   python manage.py runserver
---

## 🧪 Uso
- Autenticarse en la aplicación.

- Subir un contrato en formato compatible.

- Interactuar mediante el chat para hacer preguntas relacionadas con el contrato.
---

## 📄 Variables de entorno
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:
```python
  DB_NAME=
  DB_USER=
  DB_PASSWORD=
  DB_HOST=
  DB_PORT=
  GOOGLE_AI_API_KEY=
```
  ---

## 📜 Licencia
Este proyecto está bajo la licencia MIT.
   ---

## 👤 Créditos
Desarrollado por Ángel Bracamonte
GitHub: @angluisb
---
