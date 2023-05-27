from tkinter import Tk, Button, Label, filedialog, OptionMenu, StringVar
from PIL import Image
import os

def converter_imagens():
    # Abre a caixa de diálogo para selecionar a pasta
    pasta = filedialog.askdirectory()

    if pasta:
        pasta_saida = os.path.join(pasta, "saida")
        # Cria a pasta de saída, se não existir
        os.makedirs(pasta_saida, exist_ok=True)

        # Percorre todos os arquivos na pasta
        for nome_arquivo in os.listdir(pasta):
            caminho_imagem = os.path.join(pasta, nome_arquivo)

            # Verifica se o arquivo é uma imagem
            if os.path.isfile(caminho_imagem) and nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Obtém o caminho de saída com a nova extensão
                caminho_saida = os.path.join(pasta_saida, nome_arquivo.rsplit('.', 1)[0] + '.' + nova_extensao.get())

                # Converte a extensão da imagem
                imagem = Image.open(caminho_imagem)
                imagem.save(caminho_saida, quality='keep', subsampling=0)

        label_status["text"] = "Conversão de imagens concluída!"

# Cria a janela principal
janela = Tk()
janela.title("Conversão de Extensões de Imagem")
janela.geometry("400x200")
janela.configure(bg="#f0f0f0")

# Label para instruções
label_instrucoes = Label(janela, text="Selecione a pasta e a nova extensão", font=("Arial", 12), bg="#f0f0f0")
label_instrucoes.pack(pady=10)

# Dropdown para selecionar a nova extensão
nova_extensao = StringVar(janela)
nova_extensao.set("jpg")  # Valor padrão
dropdown_extensao = OptionMenu(janela, nova_extensao, "jpg", "png", "gif")
dropdown_extensao.configure(width=10)
dropdown_extensao.pack()

# Botão para selecionar a pasta e converter as imagens
botao_selecionar = Button(janela, text="Selecionar Pasta", font=("Arial", 12), bg="#ffffff", padx=10, pady=5, relief="solid", command=converter_imagens)
botao_selecionar.pack(pady=10)

# Label para exibir o status da conversão
label_status = Label(janela, text="", font=("Arial", 12), bg="#f0f0f0")
label_status.pack()

# Executa o loop principal da interface gráfica
janela.mainloop()
