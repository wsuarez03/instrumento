import pandas as pd
import requests
import json

# Enlace de descarga directa del Excel desde OneDrive
url = "https://valserindustriales-my.sharepoint.com/personal/tecnicodeservicios_valserindustriales_com/_layouts/15/download.aspx?share=EVnbovyqvexMmz6vKmaa6tcBwm4y-ES_mWUBwaOX76jhPg"

# Descargar el Excel
response = requests.get(url)
if response.status_code == 200:
    with open("temp.xlsx", "wb") as f:
        f.write(response.content)
    print("✅ Excel descargado correctamente")
else:
    raise Exception("❌ Error al descargar el Excel")

# Leer y convertir a JSON
df = pd.read_excel("temp.xlsx", dtype=str)
datos = df.to_dict(orient="records")

# Guardar como instrumentos.json
with open("instrumentos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)

print("✅ JSON generado correctamente")
