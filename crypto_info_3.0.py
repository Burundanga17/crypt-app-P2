import requests
import matplotlib.pyplot as plt
from datetime import datetime

def obtener_precio_crypto(crypto_id, moneda_fiat):
    """
    Consulta la API de CoinGecko para obtener el precio actual de una cripto,
    junto con capitalización de mercado y volumen.
    """
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={moneda_fiat}&ids={crypto_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # lanza error si status != 200

        data = response.json()
        if data:
            info = data[0]
            precio = info["current_price"]
            market_cap = info["market_cap"]
            volumen = info["total_volume"]

            return (
                f"El precio actual de {crypto_id.capitalize()} es {precio} {moneda_fiat.upper()}.\n"
                f"Capitalización de mercado: {market_cap} {moneda_fiat.upper()}.\n"
                f"Volumen total: {volumen} {moneda_fiat.upper()}."
            )
        else:
            return "No se encontró información para esa criptomoneda."

    except requests.exceptions.Timeout:
        return "Error: la solicitud a la API excedió el tiempo de espera."
    except requests.exceptions.ConnectionError:
        return "Error: no se pudo establecer conexión con la API."
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return "Error 404: criptomoneda no encontrada."
        else:
            return f"Error HTTP: {e}"
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

def graficar_evolucion(crypto_id, moneda_fiat, dias=7):
    """
    Consulta la API de CoinGecko para obtener la evolución del precio
    y genera un gráfico con matplotlib.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency={moneda_fiat}&days={dias}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        precios = data.get("prices", [])

        if not precios:
            print("No se encontraron datos históricos para graficar.")
            return

        # Extraemos tiempos y valores
        tiempos = [datetime.fromtimestamp(p[0]/1000) for p in precios]
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

    except requests.exceptions.Timeout:
        print("Error: la solicitud a la API excedió el tiempo de espera.")
    except requests.exceptions.ConnectionError:
        print("Error: no se pudo establecer conexión con la API.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("Error 404: criptomoneda no encontrada.")
        else:
            print(f"Error HTTP: {e}")
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
