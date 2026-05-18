# Crypto_info

## 🎯 Narrativa del Proyecto
**Stakeholder:** Inversionista en criptomonedas que requiere información rápida y confiable para tomar decisiones de compra o venta.

**Problema/Solución:**  
Los inversionistas suelen perder tiempo buscando precios en distintas plataformas y no cuentan con una herramienta simple que muestre la evolución histórica de forma inmediata.  
**Crypto_info** resuelve este problema al permitir ingresar:
- El nombre de la criptomoneda (ej: bitcoin, ethereum).
- La moneda fiat deseada (ej: usd, eur, clp).
- El rango de días para graficar (ej: 7, 30, 90).  

El sistema devuelve el precio actual, capitalizacion de mercado, volumen total y un gráfico de evolución del valor en el período solicitado.

---

## ⚙️ Configuración

No se requiere clave de API ni variables de entorno.  
Solo es necesario instalar las dependencias listadas en `requirements.txt`.

---

## 🚀 Ejecución (modo local)
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
