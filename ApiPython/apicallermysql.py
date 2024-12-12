import requests
codigo = int(input("Ingrese código postal: "))

url = f"http://localhost/apis/colonias.php?codigo={codigo}"

response = requests.get(url)

try:
    responsedata = response.json()
    print(f'El resultado es {responsedata["data"]}')
except ValueError:
    print("La respuesta no es un JSON válido.")