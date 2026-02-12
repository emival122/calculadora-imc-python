import customtkinter as ctk

# ---------------- CONFIGURAÇÕES ----------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Calculadora de IMC")
janela.geometry("440x650")
janela.resizable(False, False)

# ---------------- CORES ----------------

COR_MAGREZA = "#3498db"
COR_NORMAL = "#2ecc71"
COR_SOBREPESO = "#f1c40f"
COR_OBESIDADE = "#e74c3c"
COR_PRIMARIA = "#1f6aa5"
COR_CARD = "#eef1f5"

# ---------------- GRID ----------------

janela.grid_columnconfigure(0, weight=1)

# ---------------- HEADER ----------------

header = ctk.CTkFrame(janela, height=140, corner_radius=20)
header.grid(row=0, column=0, padx=20, pady=(20, 15), sticky="ew")
header.grid_propagate(False)

titulo = ctk.CTkLabel(
    header,
    text="📊 Calculadora de IMC",
    font=("Helvetica", 30, "bold"),
    text_color=COR_PRIMARIA
)
titulo.pack(pady=(35, 5))

subtitulo = ctk.CTkLabel(
    header,
    text="Descubra seu Índice de Massa Corporal",
    font=("Helvetica", 14),
    text_color="#555"
)
subtitulo.pack()

# ---------------- CONTEÚDO ----------------

conteudo = ctk.CTkFrame(janela, corner_radius=20)
conteudo.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")
conteudo.grid_columnconfigure(0, weight=1)

# ---------------- ENTRADAS ----------------


def criar_label(texto, row):
    ctk.CTkLabel(
        conteudo,
        text=texto,
        font=("Helvetica", 14, "bold")
    ).grid(row=row, column=0, padx=25, pady=(15, 5), sticky="w")


criar_label("Peso (Kg)", 0)

entrada_peso = ctk.CTkEntry(
    conteudo,
    placeholder_text="Ex: 70",
    height=45,
    font=("Helvetica", 14)
)
entrada_peso.grid(row=1, column=0, padx=25, pady=(0, 10), sticky="ew")

criar_label("Altura (m)", 2)

entrada_altura = ctk.CTkEntry(
    conteudo,
    placeholder_text="Ex: 1.75",
    height=45,
    font=("Helvetica", 14)
)
entrada_altura.grid(row=3, column=0, padx=25, pady=(0, 15), sticky="ew")

# ---------------- RESULTADO (CARD) ----------------

card_resultado = ctk.CTkFrame(
    conteudo,
    corner_radius=15,
    fg_color=COR_CARD
)
card_resultado.grid(row=4, column=0, padx=25, pady=25, sticky="ew")

resultado = ctk.CTkLabel(
    card_resultado,
    text="Informe seus dados",
    font=("Helvetica", 16, "bold"),
    justify="center"
)
resultado.pack(pady=30)

# ---------------- FUNÇÕES ----------------


def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza", COR_MAGREZA
    elif imc < 25:
        return "Normal", COR_NORMAL
    elif imc < 30:
        return "Sobrepeso", COR_SOBREPESO
    else:
        return "Obesidade", COR_OBESIDADE


def calcular_imc():
    try:
        peso = float(entrada_peso.get().replace(",", "."))
        altura = float(entrada_altura.get().replace(",", "."))

        if peso <= 0 or altura <= 0:
            raise ValueError

        imc = peso / (altura ** 2)
        classificacao, cor = classificar_imc(imc)

        resultado.configure(
            text=f"IMC: {imc:.2f}\n{classificacao}",
            text_color=cor
        )

    except ValueError:
        resultado.configure(
            text="❌ Digite valores válidos",
            text_color=COR_OBESIDADE
        )

# ---------------- BOTÃO ----------------


botao_calcular = ctk.CTkButton(
    conteudo,
    text="Calcular IMC",
    height=50,
    font=("Helvetica", 16, "bold"),
    command=calcular_imc
)
botao_calcular.grid(row=5, column=0, padx=25, pady=(0, 25), sticky="ew")

# ---------------- LOOP ----------------

janela.mainloop()
