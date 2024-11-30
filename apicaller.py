import requests
numero1 = float(input("Ingrese número 1: "))
numero2 = float(input("Ingrese número 2: "))
url = f"http://localhost/apis/suma.php?numero1={numero1}&numero2={numero2}"
response = requests.post(url)
responsedata = response.json()
#print (responsedata)
print (f"El resultado es: {responsedata['result']}")