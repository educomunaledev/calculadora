import tkinter as tk

# Função para atualizar a entrada
def click_botao(valor):
    current = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, current + valor)

# Função para calcular a expressão
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Campo de entrada
entrada = tk.Entry(root, width=16, font=('Arial', 24), bd=5, insertwidth=4, borderwidth=4)
entrada.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4)
]

for (texto, linha, coluna, *colspan) in botoes:
    if texto == '=':
        b = tk.Button(root, text=texto, padx=20, pady=20, command=calcular)
    elif texto == 'C':
        b = tk.Button(root, text=texto, padx=20, pady=20, command=limpar)
    else:
        b = tk.Button(root, text=texto, padx=20, pady=20, command=lambda t=texto: click_botao(t))
    
    if colspan:
        b.grid(row=linha, column=coluna, columnspan=colspan[0])
    else:
        b.grid(row=linha, column=coluna)

root.mainloop()
