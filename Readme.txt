1. API y resiliencia
Usé una API de tipo de cambio para convertir dólares a quetzales en tiempo real.
La elegí porque era fácil de integrar y me daba el valor actualizado del dólar.
Para manejar errores, hice lo siguiente:
Separé la lógica en un servicio
Usé try/except para evitar que la app se caiga si la API falla
En caso de error, se puede controlar el flujo para no romper las transacciones


2. Decisiones técnicas
Usé estas tecnologías:
FastAPI para el backend porque es rápido y fácil de usar
SQLAlchemy para manejar la base de datos de forma ordenad
PostgreSQL como base de datos
JWT para autenticación
bcrypt para encriptar contraseñas
React con Vite para el frontend porque es ligero y rápido
Axios para conectar frontend con backend
Recharts para mostrar gráficos
Las elegí porque son herramientas modernas, estables y muy usadas en proyectos reales.

3. Arquitectura
El backend lo organicé por módulos:
routes → endpoints de la API
services → lógica como conversión de moneda
models → tablas de la base de datos
core → seguridad y autenticación

Esto ayuda a que el proyecto sea más ordenado y fácil de escalar.

4. Lógica de negocio
La conversión de moneda se hace en el backend cuando se crea la transacción.
Una vez guardado el valor (USD y GTQ), ya no cambia aunque el tipo de cambio cambie después.
Esto asegura que los datos sean consistentes e históricos.

5. Retos
Lo más complicado fue:
Irónicamente fue en la parte más facil que es git, comencé a hacer todo el repositorio dentro del BackEnd y eso me atrazó horas,
tuve que regresar a versiones anteriores porque se me hizo un caos por mala gestión y apesar que no terminé el Front, el back
funciona lo suficientemente bien


6. Mejora futura
Si tuviera más tiempo, mejoraría:
Seguridad con refresh tokens
Mejor diseño en frontend
Validaciones más fuertes en el backend

Tests automáticos
Logs para ver errores del sistema
Cache del tipo de cambio para optimizar la API
Despliegue en la nube
