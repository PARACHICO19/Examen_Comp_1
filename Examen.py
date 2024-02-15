import tkinter as tk
from tkinter import *
import ply.lex as lex

tokens = ['Delimitador','Error','Reservado','Numero','Operador','Identificador','Tipo','Cadena']

def t_Delimitador(t):
    r'[\(\)\{\}\[\];]'
    return t

def t_Operador(t):
    r'(\+|\-|=|\*|\/|\+\+)+'
    return t

def t_Identificador(t):
    r'\b(suma|progrma|a|b|c|programa)\b'
    t.type = 'Identificador'
    t.value = t.value.strip()
    return t

def t_Cadena(t):
    r'\b"([^"]+)"\b'
    t.type = 'Cadena'
    t.value = t.value.strip()
    return t

def t_Tipo(t):
    r'\b(int|double|decimal|float|str|char)\b'
    t.type = 'Tipo'
    t.value = t.value.strip()
    return t  

def t_Reservado(t):
    r'\b(for|do|while|else|if|main|read|printf|end|static|void|public)\b'
    t.type = 'Reservado'
    t.value = t.value.strip()
    return t

def t_Numero(t):
    r'(\d+)(\.?\d*)'
    t.value = float(t.value)
    return t

def t_error(t):
    error_texto.insert(tk.END, f"Carácter no válido: '{t.value[0]}'\n")
    t.lexer.skip(1)


lexer = lex.lex()

class Lexer:
    def __init__(self, data):
        self.lexer = lex.lex()
        self.lexer.input(data)
    
    def reset(self, line):
        line = line.strip()
        self.lexer.input(line)


def analizar():
    borrar_resultados()
    lexer = Lexer(entrada_texto.get("1.0", "end-1c"))
    line_number = 1
    total_tokens = 0
    for linea in entrada_texto.get("1.0", "end-1c").splitlines():
        lexer.reset(linea)
        while True:
            token = lexer.lexer.token()
            if not token:
                break      # No more input
            total_tokens += 1
            resultado_token.insert(tk.END, f"{token.type}\n")
            resultado_lexema.insert(tk.END, f"{token.value}\n")
            resultado_pos.insert(tk.END, f"{token.lexpos}\n")
            resultado_lineno.insert(tk.END, f"{line_number}\n")
            resultado_total.insert(tk.END, f"Total de tokens: {total_tokens}\n")
            if token.type == 'ERROR':
                error_texto.insert(tk.END, f"Carácter No álido: '{token.value[0]}' En La línea {line_number}\n")
        line_number += 1
        

def borrar_resultados():
    resultado_token.delete("1.0", tk.END)
    resultado_lexema.delete("1.0", tk.END)
    resultado_pos.delete("1.0", tk.END)
    resultado_lineno.delete("1.0", tk.END)
    resultado_total.delete("1.0", tk.END)

    error_texto.delete("1.0", tk.END)

def borrar():
    entrada_texto.delete("1.0", tk.END)
    borrar_resultados()

ventana = tk.Tk()
ventana.geometry("800x800")
ventana.resizable(width=False, height=False)
ventana.title ("Analizador Lexico")
ventana.config(bg="#5DE16F")

##Entrada de texto

entrada_texto = tk.Text(ventana, font=("Arial",12), bg="white", fg="black", height=10, width=40)
entrada_texto.place(x=20, y=60, width = 350, height=380)
entrada_texto.configure(insertbackground="black")

##Etiquetas para marcar columnas de resultados

reja_token = tk.Label(ventana, text= "Token", font=("Arial",12), bg="#B0455C", fg="black")
reja_token.place (x=420, y=60, width = 106, height=15)

reja_lex = tk.Label(ventana, text= "Lex", font=("Arial",12), bg="#B0455C", fg="black")
reja_lex.place (x=528, y=60, width = 86, height=15)

reja_lineno = tk.Label(ventana, text= "Linea", font=("Arial",12), bg="#B0455C", fg="black")
reja_lineno.place (x=616, y=60, width = 86, height=15)

reja_pos = tk.Label(ventana, text= "Poscicion", font=("Arial",12), bg="#B0455C", fg="black")
reja_pos.place (x=704, y=60, width = 86, height=15)

##Resultados

resultado_token = tk.Text(ventana, font=("Arial",10), bg="#E1C354", fg="black", height=10, width=40)
resultado_token.place(x=420, y=77, width = 106, height=280)

resultado_lexema = tk.Text(ventana, font=("Arial",10), bg="#E1C354", fg="black", height=10, width=40)
resultado_lexema.place(x=528, y=77, width = 86, height=280)

resultado_lineno = tk.Text(ventana, font=("Arial",10), bg="#E1C354", fg="black", height=10, width=40)
resultado_lineno.place(x=616, y=77, width = 86, height=280)

resultado_pos = tk.Text(ventana, font=("Arial",10), bg="#E1C354", fg="black", height=10, width=40)
resultado_pos.place(x=704, y=77, width = 86, height=280)


##Total

reja_pos = tk.Label(ventana, text= "Total", justify= ["left"], font=("Arial",12), bg="#B0455C", fg="black")
reja_pos.place (x=420, y=360, width = 370, height=23)

resultado_total = tk.Text(ventana, font=("Arial",10), bg="#E1C354", fg="black", height=10, width=40)
resultado_total.place(x=420, y=380, width = 370, height=280)


##Errores

reja_pos = tk.Label(ventana, text= "Errores", justify= ["left"], font=("Arial",12), bg="#B0455C", fg="black")
reja_pos.place (x=20, y=500, width = 370, height=23)

error_texto = tk.Text(ventana, font=("Arial",10), bg="white", fg="black", height=10, width=40)
error_texto.place(x=20, y=520, width = 370, height=120)



##Botones

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial",15),bg="#24B2C6",fg="black",command=analizar)
boton_analizar.place(x=160, y=450)

boton_borrar = tk.Button(ventana, text="Borrar", font=("Arial",15),bg="#24B2C6",fg="black",command = borrar)
boton_borrar.place(x=160, y=650)

ventana.mainloop()