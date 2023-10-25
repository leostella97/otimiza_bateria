import tkinter as tk
import tkinter.font as tkfont
import psutil
import time

# Função para carregar a bateria até 85%
def carregar_bateria():
    # Obtém o status atual da bateria
    bateria = psutil.sensors_battery()

    # Se a bateria estiver abaixo de 85%, carrega até 85%
    if bateria.percent < 85:
        bateria.charge()

# Função para descarregar a bateria até 80%
def descarregar_bateria():
    # Obtém o status atual da bateria
    bateria = psutil.sensors_battery()

    # Se a bateria estiver acima de 80%, descarrega até 80%
    if bateria.percent > 80:
        bateria.discharge()

# Função para iniciar o script de carregamento
def iniciar_script():
    # Carrega a bateria até 85%
    carregar_bateria()

    # Enquanto a bateria estiver acima de 80%, descarrega até 80%
    while bateria.percent > 80:
        descarregar_bateria()
        time.sleep(60)

    # Volta a carregar a bateria até 85%
    carregar_bateria()

# Função para sair do programa
def sair():
    janela.destroy()

# Cria a janela principal
janela = tk.Tk()
janela.title("Otimização de carregamento")

# Cria uma fonte bold de tamanho 16
fonte = tkfont.Font(family="Helvetica", size=16, weight="bold")

# Cria o texto no topo da janela
texto_topo = tk.Label(janela, text="Otimização de carregamento", font=fonte)
texto_topo.pack()

# Cria o texto no centro da janela
texto_centro = tk.Label(janela, text="""
Clique no botão INICIAR para otimizar a bateria de seu notebook
O carregamento vai somente até 85% e, quando atingir esse valor, 
  desce até 80% para carregar até 85% novamente
Ótimo para a vida útil de sua bateria""")
texto_centro.pack()

# Cria o botão INICIAR
botao_iniciar = tk.Button(janela, text="INICIAR", command=iniciar_script)
botao_iniciar.pack()

# Cria o botão SAIR
botao_sair = tk.Button(janela, text="SAIR", command=sair)
botao_sair.pack()

# Cria o texto no rodapé da janela
texto_rodape = tk.Label(janela, text="Desenvolvido por Leonardo Stella", font=("Helvetica", 16, "italic"))
texto_rodape.pack()

# Cria o comportamento da janela quando minimizada
janela.protocol("WM_DELETE_WINDOW", lambda: None)

# Define o comportamento da janela quando minimizada
janela.wm_withdraw()

# Mostra a janela
janela.mainloop()
