import tkinter as tk
from tkinter import ttk  # Importa o submódulo ttk

# Cria a janela principal (esta é sempre tk.Tk())
root = tk.Tk()
root.title("Exemplo de Ttk")

# --- Widgets Clássicos do Tkinter ---
# Eles têm uma aparência antiga e simples
label_old = tk.Label(root, text="Widget Clássico")
label_old.pack(pady=5)

button_old = tk.Button(root, text="Botão Clássico")
button_old.pack()

# --- Widgets Modernos do Ttk ---
# Eles herdam o visual do seu sistema operacional
label_new = ttk.Label(root, text="Widget com Ttk")
label_new.pack(pady=5)

button_new = ttk.Button(root, text="Botão com Ttk")
button_new.pack()

root.mainloop()
