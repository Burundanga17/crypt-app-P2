import requests
import matplotlib.pyplot as plt
from datetime import datetime

def obtener_precio_crypto(crypto_id, moneda_fiat):
    """
    Consulta la API de CoinGecko para obtener el precio actual de una cripto.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={moneda_fiat}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                precio = data[crypto_id][moneda_fiat]
                return f"El precio actual de {crypto_id.capitalize()} es {precio} {moneda_fiat.upper()}."
            else:
                return "No se encontró información para esa criptomoneda."
        else:
            return f"Error al conectar con la API. Código de estado: {response.status_code}"
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

def graficar_evolucion(crypto_id, moneda_fiat, dias=7):
    """
    Consulta la API de CoinGecko para obtener la evolución del precio
    y genera un gráfico con matplotlib.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency={moneda_fiat}&days={dias}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            precios = data["prices"]  # Lista de [timestamp, precio]

            # Extraemos tiempos y valores
            tiempos = [datetime.fromtimestamp(p[0]/1000) for p in precios]  # convertir ms → segundos
            valores = [p[1] for p in precios]

            # Graficamos
            plt.figure(figsize=(10,5))
            plt.plot(tiempos, valores, label=f"{crypto_id.capitalize()} en {moneda_fiat.upper()}")
            plt.title(f"Evolución de {crypto_id.capitalize()} en {moneda_fiat.upper()} (últimos {dias} días)")
            plt.xlabel("Fecha")
            plt.ylabel(f"Precio ({moneda_fiat.upper()})")
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print(f"Error al conectar con la API. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    cripto = input("Ingresa el nombre de la cripto (ej: bitcoin): ").lower()
    moneda = input("Ingresa la moneda (ej: usd, eur, clp): ").lower()
    dias = input("Ingresa cantidad de días para el gráfico (ej: 7, 30, 90): ")

    print("\nConsultando...")
    resultado = obtener_precio_crypto(cripto, moneda)
    print(resultado)

    print("\nGenerando gráfico...")
    graficar_evolucion(cripto, moneda, int(dias))
