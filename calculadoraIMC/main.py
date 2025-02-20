import customtkinter as ctk

################# CORES PARA UTILIZAR(PODE MODIFICAR AO GOSTO SEU) ################
cor0 = "#2C3E50" # AZUL ESCURO PARA TEXTO E ROTULOS (MODERNO)
cor1 = "#ECF0F1" # CINZA CLARO PARA FUNDO E TEXTO (LIMPO LEGIVEL)
cor2 = "#E5E8E8" # AZUL PARA BOTOES (CALMO E MODERNO)
cor3 = "#E5E8E8" # CINZA CLARO PARA FUNDO DA JANELA
cor4 = "#137bc1" # AZUL PARA DETALHES E BOTÃO
cor5 = "#d5dbdc" # CINZA PARA TEXTO SECUNDARIO

ctk.set_appearance_mode("light") # MANTER NO PADRÃO CLARO

janela = ctk.CTk()
janela.title("Calculadora de IMC")
janela.geometry("440x540")
janela.configure(fg_color = cor3)

# DIVIDINDO A JANELA sup
quadro_superior = ctk.CTkFrame(janela, width=400, height=90, fg_color = cor5, corner_radius= 15)
quadro_superior.grid(row=0, column=0, sticky= "nsew", padx=20, pady=20)

# DIVIDINDO A JANELA inf
quadro_inferior = ctk.CTkFrame(janela, width=400, height=380, fg_color = cor5, corner_radius= 15)
quadro_inferior.grid(row=1, column=0, sticky= "nsew", padx=20, pady=20)

# CONFIGURANDO QUADRO SUPERIOR
nome_app = ctk.CTkLabel(quadro_superior, text="CALCULADORA DE IMC", text_color = cor4, anchor="center", font=("Helvetica", 30, "bold"))
nome_app.place(x=0, y=25, relwidth=1)

# FUNÇÃO PARA CALCULAR O IMC:
def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get()) ** 2
    resultado = peso / altura

    if resultado < 18.6:
        l_texto_resultado.configure(text = "CUIDADO! VOCÊ ESTÁ ABAIXO DO PESO")
    elif resultado >= 18.5 and resultado < 24.9:
        l_texto_resultado.configure(text = "SEU PESO ESTÁ NORMAL")
    elif resultado >= 25 and resultado < 29.9:
        l_texto_resultado.configure(text = "CUIDADO! VOCÊ ESTÁ ACIMA DO PESO")
    else:
        l_texto_resultado.configure(text = "RISCO! VOCÊ ESTÁ COM OBESIDADE")
        
    l_resultado.configure(text ="{:.{}f}".format(resultado,2))
    

# CONFIGURANDO QUADRO INFERIOR
l_peso = ctk.CTkLabel(quadro_inferior, text="Digite seu peso (Kg)", text_color = cor0, font=("Helvetica", 14))
l_peso.grid(row=0, column=0, sticky= "nw", padx=15, pady=15)

e_peso = ctk.CTkEntry(quadro_inferior, width= 180, font=("Helvetica", 16), justify = "center", corner_radius = 12)
e_peso.grid(row=0, column=1, sticky= "nsew", padx=15, pady=15)


l_altura = ctk.CTkLabel(quadro_inferior, text="Digite sua altura (m)", text_color = cor0, font=("Helvetica", 14))
l_altura.grid(row=1, column=0, sticky= "nw", padx=15, pady=15)

e_altura = ctk.CTkEntry(quadro_inferior, width= 180, font=("Helvetica", 16), justify = "center", corner_radius = 12)
e_altura.grid(row=1, column=1, sticky= "nsew", padx=15, pady=15)

# CONFIGURAR O RESULTADO
l_resultado = ctk.CTkLabel(quadro_inferior, text = "", width = 5, height = 1,
                                            text_color = cor0,
                                            font=("Helvetica", 32, "bold"), 
                                            anchor = "center", 
                                            corner_radius = 12)
l_resultado.grid(row=2, column=0, columnspan = 2, padx=15, pady=30)


l_texto_resultado = ctk.CTkLabel(quadro_inferior, text = "",
                                            text_color = cor0,
                                            font=("Helvetica", 16), 
                                            anchor = "center",)
l_texto_resultado.grid(row=3, column=0, columnspan = 2, padx=15, pady=15)

# CONFIGURAR BOTÃO
b_calcular = ctk.CTkButton(quadro_inferior, text = "Calcular",
                                            width = 180, height = 50,
                                            font = ("Helvetica", 16, "bold"), 
                                            fg_color = "#4893c5",
                                            hover_color = "#137bc1", 
                                            corner_radius= 12, command = calcular)
b_calcular.grid(row=4, column=0, columnspan = 2, padx=15, pady=25)


janela.mainloop()