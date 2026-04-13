Sistema de Remesas Fullstack
Este proyecto es una aplicación completa para manejo de remesas con conversión de moneda (USD → GTQ), autenticación JWT, control de roles y visualización de historial con gráficos.

Está construido con:
- Backend: FastAPI
- Frontend: React + Vite
- Base de datos: PostgreSQL
- Docker (todo el sistema se levanta con un solo comando)


¿Qué puedes hacer en esta aplicación?
- Iniciar sesión con usuarios
- Enviar dinero (rol HIJO)
- Solicitar dinero (rol RECEPTOR)
- Ver historial de remesas
- Ver gráfico de transacciones
- Todo protegido con autenticación JWT


REQUISITOS

Antes de empezar necesitas tener instalado:
- Docker
- Docker Compose

CÓMO EJECUTAR EL PROYECTO

1. Clonar el proyecto

```bash id="clonar"
git clone https://github.com/PabloJGB/Proyecto_Remesas__Cliente_Alex.git
cd Proyecto_Don_Alex

Levantar todo con Docker

Desde la raíz del proyecto ejecutar:
docker-compose up --build

Esperar a que cargue y probar

Backend → http://localhost:8000
Frontend → http://localhost:5173
Docs API → http://localhost:8000/docs

PARA ACCEDER AL SISTEMA
Frontend (Aplicación)
http://localhost:5173
Backend (API Swagger)
http://localhost:8000/docs

CREDENCIALES DE PRUEBA
Usuario HIJO (puede enviar dinero)
Email: hijo@mail.com
Password: 123
Rol: HIJO

Usuario RECEPTOR (puede solicitar dinero)
Email: alex@mail.com
Password: 123
Rol: RECEPTOR

CÓMO PROBAR EL SISTEMA
Paso 1
Entrar a:
http://localhost:5173
Paso 2
Iniciar sesión con cualquiera de los usuarios
Paso 3
Probar funcionalidades: