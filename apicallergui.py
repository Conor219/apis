from tkinter import Tk, Label, Entry, Button, messagebox
import requests
#Declaramos la función
def LlamarApi():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        url = f"http://localhost/apis/suma.php?numero1={numero1}&numero2={numero2}"
        response = requests.get(url)
        responsedata = response.json()
        label3["text"] = f'El resultado es {responsedata["result"]}'
    except ValueError:
        label3["text"] = "La respuesta no es un JSON válido."

ventana = Tk()
ventana.geometry("300x200")
ventana.title("Actividad 9: API - Python - GUI")
ventana["bg"] = "#FE0FE0"

label1 = Label(ventana, text = "Numero 1")
label1.place(x = 30, y = 30)
num1 = Entry(ventana)
num1.place(x = 100, y = 30)

label2 = Label(ventana, text = "Numero 2")
label2.place(x = 30, y = 60)
num2 = Entry(ventana)
num2.place(x = 100, y = 60)

button = Button(ventana, text = "Obtener suma", command=LlamarApi)
button.place(x = 30, y = 90)

label3 = Label(ventana, text = "Cadena vacía")
label3.place(x = 30, y = 130)

# Esta línea siempre va al final del archivo.
ventana.mainloop()