# client.py
import requests
import datetime
import time

SERVER_URL = "http://server:5000/time"  # URL del servidor de tiempo

def synchronize_time():
    t1 = datetime.datetime.now()  # Marca el tiempo antes de la petición
    response = requests.get(SERVER_URL)
    t2 = datetime.datetime.now()  # Marca el tiempo después de la petición

    if response.status_code == 200:
        server_time = datetime.datetime.fromisoformat(response.json()["server_time"])
        # Calcula el retardo de red
        network_delay = (t2 - t1) / 2
        adjusted_time = server_time + network_delay
        print(f"Tiempo ajustado del cliente: {adjusted_time}")
    else:
        print("Error al contactar con el servidor.")

if __name__ == "__main__":
    while True:
        synchronize_time()
        time.sleep(5)  # Repite cada 5 segundos
