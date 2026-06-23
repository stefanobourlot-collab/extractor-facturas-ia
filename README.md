# Extractor de Datos de Comprobantes con IA 🚀

Este proyecto utiliza Python y la última API de **Gemini** para leer imágenes de tickets o facturas fiscales y estructurar automáticamente toda su información en un formato JSON limpio y estandarizado utilizando **Pydantic**.

## ✨ Características
- Extracción precisa de datos clave: Proveedor, CUIT, Fecha y Monto Total.
- Desglose detallado de los ítems de la factura (descripción, cantidad y precio unitario).
- Validación estricta de datos mediante modelos estructurados de Pydantic.
- Manejo seguro de credenciales mediante variables de entorno (`.env`) para evitar la filtración de llaves de API.

## 🛠️ Requisitos e Instalación

1. **Clonar el repositorio:**
```bash
   git clone [https://github.com/stefanobourlot-collab/extractor-facturas-ia.git](https://github.com/stefanobourlot-collab/extractor-facturas-ia.git)
   cd extractor-facturas-ia

Crear e iniciar el entorno virtual (Recomendado):

python -m venv venv
   .\venv\Scripts\activate

   Instalar las dependencias necesarias:

   pip install google-genai pydantic pillow python-dotenv

   Configurar las credenciales:
Creá un archivo llamado .env en la raíz del proyecto y agregá tu API Key de Google AI Studio:

GEMINI_API_KEY=tu_api_key_aqui

🚀 Uso
1. Colocá la imagen del comprobante o ticket que quieras procesar en la raíz del proyecto.

2. Asegurate de apuntar a esa imagen en tu script app.py.

3. Ejecutá el programa desde la consola:

python app.py

📋 Ejemplo de Salida (JSON estructurado)

JSON
{
  "proveedor": "FARMACIA YRIGOYEN",
  "cuit": "27230960116",
  "fecha": "18/05/2026",
  "monto_total": 21657.10,
  "items": [
    {
      "descripcion": "CORTICOSAN 50 mg comp. x 30",
      "cantidad": 1,
      "precio_unitario": 26653.00
    },
    {
      "descripcion": "DESCUENTO SOBRE ULTI",
      "cantidad": 1,
      "precio_unitario": -7995.90
    }
  ]
}
