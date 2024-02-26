"""
Instale para utilização: sudo apt-get install python3-tk

* digitar apenas uma palavra, sem caracteres especiais

"""


# 1.importando módulos

from tkinter import *
import base64

# 2.Criação de tela de display

# Janela de inicialização - root
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.config(bg='#3299CC')

# Título da janela
root.title('Codificação de Descodificação')

# Label - Etiquetas

Label(root, text='CODIFICAR / DESCODIFICAR', font='arial 20 bold').pack()

Label(root, text='Guilherme S.', font='arial 20 bold').pack(side=BOTTOM)

# 3.Definição de variáveis

mensagem = StringVar()
chave_privada = StringVar()
modo = StringVar()
resultado = StringVar()


# 4.Definindo Funções

# Função de Codificação

def codificar(chave, mensagem):
    cod = []
    for i in range(len(mensagem)):
        chave_cod = chave[i % len(chave)]
        cod.append(chr((ord(mensagem[i]) + ord(chave_cod)) % 256))

    return base64.urlsafe_b64encode("".join(cod).encode()).decode()


# Função de Descodificação

def descodificar(chave, mensagem):
    desc = []
    mensagem = base64.urlsafe_b64decode(mensagem).decode()
    for i in range(len(mensagem)):
        chave_cod = chave[1 % len(chave)]
        desc.append(chr((256 + ord(mensagem[i]) - ord(chave_cod)) % 256))

    return "".join(desc)


# Função escolher o modo

def Mode():
    if (modo.get() == 'e'):
        resultado.set(codificar(chave_privada.get(), mensagem.get()))
    elif (modo.get() == 'd'):
        resultado.set(descodificar(chave_privada.get(), mensagem.get()))
    else:
        resultado.set("Seleção Inválida")


# Função de saida da Janela
def saida():
    root.destroy()


# Função de resetar

def resetar():
    mensagem.set("")
    chave_privada.set("")
    modo.set("")
    resultado.set("")


# 4.Definir tabelas e Botões

# Mensagem
Label(root, font='arial 12 bold', text='MENSAGEM:').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=mensagem, bg='ghost white').place(x=290, y=60)

# chave
Label(root, font='arial 12 bold', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=chave_privada, bg='ghost white').place(x=290, y=90)

# Modo
Label(root, font='arial 12 bold', text='MODE(e-encode, d-decode)').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=modo, bg='ghost white').place(x=290, y=120)

# Resultado
Entry(root, font='arial 10 bold', textvariable=resultado, bg='ghost white').place(x=290, y=150)

# Botão de Resultado
Button(root, font='arial 10 bold', text='RESULTADO', padx=2, bg='LightGray', command=Mode).place(x=60, y=150)

# Botão Resetar
Button(root, font='arial 10 bold', text='RESET', width=6, command=resetar, bg='LimeGreen', padx=2).place(x=80, y=190)

# Botão de Saida
Button(root, font='arial 10 bold', text='EXIT', width=6, command=saida, bg='OrangeRed', padx=2, pady=2).place(x=180,
                                                                                                              y=190)
root.mainloop()
