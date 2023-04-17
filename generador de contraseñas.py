import random
import string
import tkinter as tk
import pyperclip
from tkinter import messagebox

# Función para generar una contraseña aleatoria
def generate_password():
    # Obtiene la longitud ingresada por el usuario desde el cuadro de entrada
    length = length_entry.get()
    
    # Validación de entrada - verifica que la longitud ingresada sea un número entero
    if not length.isdigit() or length == '':
        messagebox.showwarning("Error", "Ingrese un valor numérico para la longitud de la contraseña")
        return
    
    # Convierte la longitud a un número entero
    length = int(length)
    
    # Crea una lista de caracteres que se utilizarán para generar la contraseña
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Genera una contraseña aleatoria de la longitud especificada utilizando los caracteres de la lista
    password = ''.join(random.choice(chars) for i in range(length))
    
    # Coloca la contraseña generada en la etiqueta de texto de la ventana
    password_var.set(password)
    
    # Copia la contraseña al portapapeles
    pyperclip.copy(password)
    
    # Borra el contenido anterior del portapapeles y agrega la nueva contraseña
    root.clipboard_clear()
    root.clipboard_append(password)
    
    # Actualiza el portapapeles inmediatamente
    root.update()
    
    # Muestra un mensaje en la ventana indicando que la contraseña ha sido copiada
    messagebox.showinfo("Contraseña generada", "Contraseña copiada al portapapeles")

# Crea la ventana principal
root = tk.Tk()

# Configura el título de la ventana
root.title("Generador de contraseñas")

# Configura las dimensiones de la ventana y la hace no redimensionable
root.geometry("400x250")
root.resizable(False, False)

# Crea una etiqueta y un cuadro de entrada para que el usuario especifique la longitud de la contraseña
length_label = tk.Label(root, text="Longitud:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Crea un botón que llama a la función generate_password() cuando se hace clic en él
generate_button = tk.Button(root, text="Generar contraseña", command=generate_password)
generate_button.pack()

# Crea una etiqueta que mostrará la contraseña generada
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var)
password_label.pack()

# Inicia el bucle principal de la ventana
root.mainloop()
