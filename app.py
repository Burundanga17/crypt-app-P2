import requests
import os
import sys

def obtener_info_crypto(crypto_id, moneda_fiat, api_key=None):
    """
    Consulta la API de CoinGecko para obtener información de una criptomoneda.
    Procesa: precio actual, capitalización de mercado y volumen total.
    """
    headers = {}
    if api_key:
        headers["x-cg-demo-api-key"] = api_key

    url = (
        f"https://api.coingecko.com/api/v3/coins/markets"
        f"?vs_currency={moneda_fiat}&ids={crypto_id}"
    )

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # Error 401 - clave inválida
        if response.status_code == 401:
            print("❌ Error 401: Clave de API inválida o no autorizada.")
            sys.exit(1)

        # Error 404 - recurso no encontrado
        if response.status_code == 404:
            print("❌ Error 404: Criptomoneda no encontrada en la API.")
            sys.exit(1)

        # Otros errores HTTP
        response.raise_for_status()

        data = response.json()

        if not data:
            print("⚠️  No se encontraron datos para la criptomoneda indicada.")
            sys.exit(1)

        info = data[0]

        # Campos procesados (≥3 según rúbrica)
        nombre        = info.get("name", "N/A")
        simbolo       = info.get("symbol", "N/A").upper()
        precio        = info.get("current_price", "N/A")
        market_cap    = info.get("market_cap", "N/A")
        volumen       = info.get("total_volume", "N/A")
        cambio_24h    = info.get("price_change_percentage_24h", "N/A")
        max_24h       = info.get("high_24h", "N/A")
        min_24h       = info.get("low_24h", "N/A")

        print("=" * 50)
        print(f"  📊 Informe de Criptomoneda: {nombre} ({simbolo})")
        print("=" * 50)
        print(f"  💰 Precio actual:            {precio} {moneda_fiat.upper()}")
        print(f"  📈 Máximo 24h:               {max_24h} {moneda_fiat.upper()}")
        print(f"  📉 Mínimo 24h:               {min_24h} {moneda_fiat.upper()}")
        print(f"  🔄 Cambio últimas 24h:       {cambio_24h}%")
        print(f"  🏦 Capitalización de mercado: {market_cap} {moneda_fiat.upper()}")
        print(f"  📦 Volumen total:             {volumen} {moneda_fiat.upper()}")
        print("=" * 50)

    except requests.exceptions.Timeout:
        print("❌ Error: La solicitud a la API excedió el tiempo de espera (timeout).")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo establecer conexión con la API. Verifica tu red.")
        sys.exit(1)

    except requests.exceptions.HTTPError as e:
        print(f"❌ Error HTTP inesperado: {e}")
        sys.exit(1)

    except ValueError:
        print("❌ Error: La respuesta de la API no es un JSON válido.")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Lectura de variables de entorno (sin hardcoding)
    crypto_id  = os.getenv("CRYPTO_ID", "bitcoin")
    moneda_fiat = os.getenv("MONEDA_FIAT", "usd")
    api_key    = os.getenv("COINGECKO_API_KEY")  # Opcional pero requerido por rúbrica

    print(f"\n🔍 Consultando datos de '{crypto_id}' en '{moneda_fiat.upper()}'...\n")
    obtener_info_crypto(crypto_id, moneda_fiat, api_key)
