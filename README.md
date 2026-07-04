# 🧪 E-commerce Test Automation Framework

Framework de automatización de pruebas end-to-end para un sitio de e-commerce, construido con Selenium, Python y Pytest, siguiendo el patrón Page Object Model (POM).

## Qué prueba (11 casos)

- Login exitoso con credenciales válidas
- Login fallido con credenciales incorrectas
- Login con usuario bloqueado (locked_out_user)
- Login con campos vacíos
- Agregar múltiples productos al carrito
- Remover producto del carrito
- Ordenar productos por precio
- Flujo completo de compra (login → carrito → checkout → confirmación)
- Checkout con campos vacíos (validación de errores)
- Cancelar checkout y regresar al carrito
- Logout exitoso

## Stack técnico

- Python 3.12
- Selenium WebDriver
- Pytest + pytest-rerunfailures (reintentos automáticos ante fallos intermitentes de red)
- Page Object Model (POM)
- WebDriverWait / Expected Conditions (esperas explícitas para tests robustos)
- webdriver-manager (gestión automática del driver de Chrome)
- Captura automática de screenshots ante fallos, para depuración

## Estructura del proyecto

\```
selenium-ecommerce-testing/
├── pages/          # Page Objects (login, inventario, carrito, checkout)
├── tests/          # Casos de prueba + configuración de pytest
├── reports/        # Screenshots automáticos ante fallos
├── requirements.txt
└── README.md
\```

## Cómo correrlo

\```bash
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
pytest tests/ -v --reruns 2 --reruns-delay 2
\```

## Resultado

11/11 tests pasando, cubriendo el flujo crítico de e-commerce (autenticación, gestión de carrito, checkout y logout), con reintentos automáticos para manejar fallos intermitentes propios de pruebas end-to-end contra sitios reales.

## Autora

Camila Molina Toro — Estudiante de Ingeniería de Sistemas (UPB), enfocada en QA y desarrollo de software.
[LinkedIn](tu-link) · [GitHub](tu-link)
