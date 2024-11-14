# Backend para Pronóstico del Clima

Este proyecto es un backend desarrollado en Python con Flask, que consume la API de OpenWeatherMap para obtener el pronóstico del clima de una ciudad específica durante los próximos 4 días. La aplicación permite obtener datos como la fecha, temperatura mínima y máxima, y condiciones climáticas (soleado, nublado, lluvia, etc.) de una ciudad.

## Requisitos

- **Python 3.7 o superior**
- **Flask** (Microframework para Python)
- **Requests** (Para manejar las solicitudes HTTP)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   python3 -m venv env
   source env/bin/activate  # Para Linux/macOS
   env\Scripts\activate     # Para Windows
   flask run
  #Endpoint
  GET /weather
  curl "http://127.0.0.1:5000/weather?city=Bogota"

  ## Respuesta exitosa
  200
  ```json
  [
    {
        "condition": "nubes",
        "date": "2024-11-14",
        "temp_max": 27.81,
        "temp_min": 26.32
    },
    {
        "condition": "muy nuboso",
        "date": "2024-11-15",
        "temp_max": 26.95,
        "temp_min": 22.34
    },
    {
        "condition": "nubes",
        "date": "2024-11-16",
        "temp_max": 26.54,
        "temp_min": 22.93
    },
    {
        "condition": "nubes",
        "date": "2024-11-17",
        "temp_max": 24.62,
        "temp_min": 24.62
    }
] 
 ```
 ## Respuesta exitosa
  200
  ```json
[
    {
        "error": "No se encontró información del clima para la ciudad: los perross"
    },
    404
]
 ```
