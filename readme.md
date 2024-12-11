README - Tecnofusion 360
Descripción
Tecnofusion 360 es un proyecto dedicado a la reparación y reacondicionamiento de equipos de hardware y software, promoviendo la reutilización y sostenibilidad. Este proyecto se enfoca en la distribución asequible de computadoras reacondicionadas para reducir el desperdicio tecnológico.

El objetivo principal de Tecnofusion 360 es proporcionar una solución accesible y ecológica para los usuarios que necesitan equipos informáticos confiables y con buen rendimiento, pero sin el costo de nuevas unidades. A través del reacondicionamiento de computadoras, el proyecto busca contribuir a la sostenibilidad tecnológica y brindar opciones de hardware económico a quienes lo necesiten.

Este repositorio contiene el código fuente para el sistema de gestión de la tienda virtual, incluyendo características de venta, inventarios, administración de clientes y productos reacondicionados, así como funcionalidades para el seguimiento de reparaciones y donaciones de hardware.
Características
- **Tienda Virtual**: Sistema de gestión de productos reacondicionados, donde los usuarios pueden comprar equipos a precios accesibles.
- **Reparación de Equipos**: Funcionalidad para registrar y gestionar las reparaciones de equipos.
- **Donaciones de Hardware**: Formulario para que empresas y usuarios donen hardware a Tecnofusion 360.
- **Gestión de Clientes**: Control de datos de clientes y seguimiento de sus compras o reparaciones.
- **Gestión de Inventarios atraves del admin de django**: Administración de equipos disponibles, reparados y en reparación.
Tecnologías utilizadas
- **Django**: Framework web para la creación de aplicaciones backend.
- **HTML/CSS/JS**: Para la creación del frontend y la interacción del usuario.
- **SQLite** (por defecto) o **PostgreSQL**: Base de datos relacional para almacenar información sobre productos, reparaciones, clientes, etc.
- **pip**: Para instalar dependencias.
- **Sphinx**: Para la documentación del proyecto.
Requisitos
Asegúrate de tener instalado lo siguiente en tu entorno:

- **Python 3.8 o superior**
- **Django 5.1.1 o superior**
- **PostgreSQL** (opcional, por defecto se utiliza SQLite)
- **pip** (para instalar dependencias)
Instalación
1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/tu_usuario/Tecnofusion360.git
    cd Tecnofusion360
    ```

2. **Crea y activa un entorno virtual**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate    # Para Windows
    ```

3. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la base de datos** (si usas PostgreSQL, actualiza las configuraciones en `settings.py`):
    ```bash
    python manage.py migrate
    ```

5. **Crea un superusuario** para acceder al panel de administración de Django:
    ```bash
    python manage.py createsuperuser
    ```

6. **Inicia el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.
    
Uso
- **Acceder a la tienda**: Los usuarios pueden ver productos reacondicionados y realizar compras.
- **Registro y gestión de clientes**: Los usuarios pueden registrarse y hacer seguimiento de sus compras y reparaciones.
- **Panel de administración**: El superusuario puede gestionar productos, clientes, reparaciones y más.

Para acceder al panel de administración de Django, ve a `http://127.0.0.1:8000/admin/` e inicia sesión con las credenciales del superusuario.
Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y realiza un commit (`git commit -am 'Añadir nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Crea un pull request.
Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).
