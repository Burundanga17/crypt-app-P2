import requests

def obtener_precio_crypto(crypto_id, moneda_fiat):
    """
    Consulta la API de CoinGecko para obtener el precio de una cripto.
    crypto_id: Nombre de la cripto (ej: 'bitcoin', 'ethereum', 'solana')
    moneda_fiat: Moneda de referencia (ej: 'usd', 'eur', 'clp')
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={moneda_fiat}"
    
    try:
        response = requests.get(url)
        # Verificamos si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            data = response.json()
            
            # Verificamos si la respuesta contiene datos
            if data:
                precio = data[crypto_id][moneda_fiat]
                return f"El precio actual de {crypto_id.capitalize()} es {precio} {moneda_fiat.upper()}."
            else:
                return "No se encontró información para esa criptomoneda."
        else:
            return f"Error al conectar con la API. Código de estado: {response.status_code}"
            
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

# --- Ejemplo de uso ---
if __name__ == "__main__":
    cripto = input("Ingresa el nombre de la cripto (ej: bitcoin): ").lower()
    moneda = input("Ingresa la moneda (ej: usd, eur, clp): ").lower()
    
    print("\nConsultando...")
    resultado = obtener_precio_crypto(cripto, moneda)
    print(resultado)