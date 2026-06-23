import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from PIL import Image
from dotenv import load_dotenv

# Cargamos las variables del archivo .env automáticamente
load_dotenv()

class ItemComprobante(BaseModel):
    descripcion: str = Field(description="Descripción del artículo o servicio")
    cantidad: int
    precio_unitario: float

class FacturaEstructured(BaseModel):
    proveedor: str = Field(description="Nombre de la empresa que emite la factura")
    cuit: str = Field(description="CUIT del emisor si aplica, o número de identificación fiscal")
    fecha: str = Field(description="Fecha de emisión del comprobante")
    monto_total: float = Field(description="El monto total final de la operación")
    items: list[ItemComprobante] = Field(description="Lista de productos o servicios detallados")

def extraer_datos_factura(ruta_imagen: str):
    # Desactivamos temporalmente dotenv para que no lea el archivo .env externo
    # Inicializa el cliente pasándole tu clave REAL de Google AI Studio directamente
    client = genai.Client()
    
    try:
        imagen = Image.open(ruta_imagen)
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen en '{ruta_imagen}'")
        return

    print("Procesando la imagen con Gemini... Esperá un toque.")

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
            imagen, 
            "Extrae toda la información relevante de este comprobante de pago. Sé preciso con los montos y los ítems."
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=FacturaEstructured,
            temperature=0.1
        ),
    )

    print("\n🚀 ¡Datos extraídos con éxito!")
    print(response.text)

if __name__ == "__main__":
    RUTA_PRUEBA = "ticket.jpg" 
    extraer_datos_factura(RUTA_PRUEBA)