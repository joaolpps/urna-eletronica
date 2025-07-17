import tkinter as tk
from PIL import Image, ImageTk
import json
import os
from playsound import playsound
import tkinter.messagebox

with open("candidatos.json", "r", encoding="utf-8") as f:
    candidatos = json.load(f)

def registrar_voto(valor):
    voto = {"voto": valor}
    caminho_arquivo = "votos.json"
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            votos = json.load(f)
    else:
        votos = []
    votos.append(voto)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(votos, f, indent=4, ensure_ascii=False)

def exibir_candidato():
    numero = entrada.get()
    dados = candidatos.get(numero)
    if dados:
        nome_var.set(f"Nome: {dados['nome']}")
        partido_var.set(f"Partido: {dados['partido']}")
        caminho_imagem = os.path.join("imagens", dados['imagem'])
        if os.path.exists(caminho_imagem):
            img = Image.open(caminho_imagem)
            img = img.resize((150, 150), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            imagem_label.config(image=img_tk)
            imagem_label.image = img_tk
        else:
            nome_var.set("Candidato não encontrado")
            partido_var.set("")
            imagem_label.config(image='')
            imagem_label.image = None
    else:
        nome_var.set("Candidato não encontrado")
        partido_var.set("")
        imagem_label.config(image='')
        imagem_label.image = None

def adicionar_digito(digito):
    numero_atual = entrada.get()
    if len(numero_atual) < 2:
        entrada.delete(0, tk.END)
        novo_numero = numero_atual + str(digito)
        entrada.insert(tk.END, novo_numero)
        if len(novo_numero) == 2:
            exibir_candidato()

def limpar():
    entrada.delete(0, tk.END)
    nome_var.set("")
    partido_var.set("")
    imagem_label.config(image='')
    imagem_label.image = None

def anular():
    entrada.delete(0, tk.END)
    nome_var.set("VOTO ANULADO")
    partido_var.set("")
    imagem_label.config(image='')
    imagem_label.image = None
    registrar_voto("NULO")

def confirmar_voto():
    numero = entrada.get()
    if numero in candidatos:
        registrar_voto(numero)
        nome_var.set("VOTO CONFIRMADO")
        playsound("confirma.wav")
    elif numero.strip() == "":
        registrar_voto("BRANCO")
        nome_var.set("VOTO BRANCO")
        playsound("confirma.wav")
    else:
        registrar_voto("NULO")
        nome_var.set("VOTO NULO")
        playsound("confirma.wav")
    partido_var.set("")
    imagem_label.config(image='')
    imagem_label.image = None
    entrada.delete(0, tk.END)

def votar_branco():
    registrar_voto("BRANCO")
    nome_var.set("VOTO CONFIRMADO")
    partido_var.set("")
    imagem_label.config(image='')
    imagem_label.image = None
    entrada.delete(0, tk.END)
    playsound("confirma.wav")

def gerar_relatorio():
    if not os.path.exists("votos.json"):
        tkinter.messagebox.showinfo("Relatório", "Nenhum voto registrado.")
        return
    with open("votos.json", "r", encoding="utf-8") as f:
        votos = json.load(f)
    contagem = {}
    total_branco = 0
    total_nulo = 0
    for v in votos:
        voto = v["voto"]
        if voto == "BRANCO":
            total_branco += 1
        elif voto == "NULO":
            total_nulo += 1
        else:
            contagem[voto] = contagem.get(voto, 0) + 1
    relatorio = ""
    for numero, total in contagem.items():
        nome = candidatos.get(numero, {}).get("nome", "Desconhecido")
        relatorio += f"{numero} - {nome}: {total} voto(s)\n"
    relatorio += f"\nBranco: {total_branco} voto(s)\nNulo: {total_nulo} voto(s)"
    tkinter.messagebox.showinfo("Relatório Final", relatorio)

def encerrar_urna():
    gerar_relatorio()
    for widget in janela.winfo_children():
        widget.destroy()
    tk.Label(janela, text="FIM", font=("Arial", 40), fg="red").pack(expand=True)
    janela.update()

def limpar_votos():
    with open("votos.json", "w", encoding="utf-8") as f:
        json.dump([], f, indent=4, ensure_ascii=False)
    tkinter.messagebox.showinfo("Limpar Votos", "Todos os votos foram apagados!")

janela = tk.Tk()
janela.title("Urna Eletrônica")
janela.geometry("600x760")
janela.resizable(False, False)

menu_frame = tk.Frame(janela)
menu_frame.pack(pady=10)

tk.Button(menu_frame, text="Limpar Votos", font=("Arial", 14), command=limpar_votos).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Encerrar Urna", font=("Arial", 14), command=encerrar_urna).pack(side=tk.LEFT, padx=5)

tk.Label(janela, text="Número do candidato:", font=("Arial", 20, "bold")).pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 24), justify="center")
entrada.pack(pady=10)

info_frame = tk.Frame(janela)
info_frame.pack(pady=10)

imagem_label = tk.Label(info_frame)
imagem_label.pack(side=tk.LEFT, padx=10)

textos_frame = tk.Frame(info_frame)
textos_frame.pack(side=tk.LEFT, padx=10)

nome_var = tk.StringVar()
partido_var = tk.StringVar()

tk.Label(textos_frame, textvariable=nome_var, font=("Arial", 15, "bold")).pack()
tk.Label(textos_frame, textvariable=partido_var, font=("Arial", 15, "bold")).pack()

teclado_frame = tk.Frame(janela)
teclado_frame.pack(pady=10)

def criar_botao(numero):
    return tk.Button(teclado_frame, text=str(numero), font=("Arial", 18), width=4, height=2,
                     command=lambda: adicionar_digito(numero))

for i in range(1, 10):
    criar_botao(i).grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

criar_botao(0).grid(row=3, column=1, padx=5, pady=5)

botoes_frame = tk.Frame(janela)
botoes_frame.pack(pady=20)

tk.Button(botoes_frame, text="Branco", font=("Arial", 14, "bold"), bg="#FCFCFC", width=10, command=votar_branco).grid(row=0, column=0, padx=5)
tk.Button(botoes_frame, text="Corrige", font=("Arial", 14, "bold"), bg="#FFA500", width=10, command=limpar).grid(row=0, column=1, padx=5)
tk.Button(botoes_frame, text="Confirmar", font=("Arial", 14, "bold"), bg="#4CAF50", width=10, command=confirmar_voto).grid(row=0, column=2, padx=5)

janela.mainloop()
