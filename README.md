# 🖨️ SmartPrinter

Aplicación de escritorio desarrollada en Python para el monitoreo de impresoras en red mediante SNMP, con interfaz gráfica y panel web de administración y métricas.

---

## 🧠 Descripción de Arquitectura (C4 - Diagrama de Contenedores)

Este sistema se compone de los siguientes contenedores principales:

### 🧩 Contenedores

- **Agente Python (App de Escritorio)**  
  Aplicación instalada en estaciones de trabajo o servidores. Escanea la red vía SNMP, obtiene métricas de impresoras y guarda temporalmente los resultados en archivos `.json`.

- **API Application (Flask / FastAPI)**  
  Expone una API RESTful para recibir datos de los agentes, así como para consultar métricas desde la interfaz web. Es el core lógico del sistema.

- **Página Web de Monitoreo (HTML/CSS/JS)**  
  Interfaz de usuario web que muestra dashboards, métricas, configuración de alertas, etc.

- **Base de Datos (PostgreSQL)**  
  Almacena métricas históricas, alertas, configuración de impresoras y logs. Pensado para escalar con múltiples agentes conectados.

---

## 📁 Estructura del Proyecto
```text
SmartPrinter/
│
├── main.py              # Punto de entrada principal de la aplicación
│
├── core/                # Lógica del negocio y funcionalidades base
│   └── agent.py         # Agente que se encarga del escaneo SNMP y recolección de métricas
│
├── ui/                  # Interfaz de usuario generada o gestionada desde Qt Designer
│   ├── mainwindow.ui    # Archivo .ui diseñado con QtDesigner
│   ├── mainwindow.py    # Código mainwindow.ui compilado por uic
│   ├── recursos.qrc     # Archivo de recursos (íconos, imágenes, qss)
│   └── recourses_rc.py  # Recursos compilados por pyside6-rcc
│
├── assets/              # Recursos estáticos
│   ├── icons/           # Íconos de la aplicación
│   └── qss/             # Hojas de estilo (temas visuales)
│       ├── Ubuntu.qss
│       └── Dark.qss
│
├── utils/               # Funciones auxiliares reutilizables
│   └── utils.py         # Ej. abs_path, loaders, etc.
│
├── views/               # Vistas individuales que forman parte del StackedWidget
│   ├── dashboard.py     # Vista principal con métricas o estado general
│   └── scan_page.py     # Vista que muestra resultados del escaneo de red
│
└── README.md            # Este archivo :)
```
## 💡 Características Planeadas

✅ Escaneo automático de red para detección de impresoras SNMP

✅ Interfaz intuitiva con pestañas dinámicas (Qt Designer + PySide6)

✅ Almacenamiento local de métricas en JSON

✅ Sincronización con servidor web por API (HTTP/POST)

🔔 Alertas configurables (por temperatura, papel, tinta)

📊 Dashboard de estado general en interfaz web

 ##  🚀 Instalacion rapida
Python 3.10 o superior

PySide6 para la interfaz gráfica de escritorio

Flask o FastAPI para la API web (según backend elegido)

PostgreSQL (opcional, si se desea persistencia remota en base de datos)

 ## 🧬 Clonar el repositorio

git clone https://github.com/TuUsuario/SmartPrinter.git
cd SmartPrinter

 ## 🛠️ Instalar dependencias

pip install -r requirements.txt

## ✨ Autor

Desarrollado por **[Nicolas Arcos - Arch IT]**  
GitHub: [https://github.com/nicoarccos](https://github.com/nicoarccos)  
Contacto: [nicolas.arcos94@hotmail.com](nicolas.arcos94@hotmail.com)
