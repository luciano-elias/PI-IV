from PIL import Image
import os

def converter_extensao_imagem(caminho_entrada, caminho_saida, nova_extensao):
    imagem = Image.open(caminho_entrada)
    imagem.save(caminho_saida, quality='keep', subsampling=0, format=nova_extensao)

def converter_extensoes_em_pasta(pasta_entrada, pasta_saida, nova_extensao):
    # Cria a pasta de saída, se não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Percorre todos os arquivos na pasta de entrada
    for nome_arquivo in os.listdir(pasta_entrada):
        caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
        caminho_saida = os.path.join(pasta_saida, nome_arquivo.rsplit('.', 1)[0] + '.' + nova_extensao)

        # Verifica se o caminho é um arquivo e se é uma imagem
        if os.path.isfile(caminho_entrada) and nome_arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            converter_extensao_imagem(caminho_entrada, caminho_saida, nova_extensao)
            print(f"Imagem {nome_arquivo} convertida com sucesso!")

# Pasta de entrada contendo as imagens
pasta_entrada = r'C:\Users\pedra\PycharmProjects\converter_extensao_imagem\fotos'

# Pasta de saída para as imagens convertidas
pasta_saida = r'C:\Users\pedra\PycharmProjects\converter_extensao_imagem\convertidas'

# Nova extensão da imagem (por exemplo, 'jpg', 'png', 'gif')
nova_extensao = 'png'

# Converter as imagens na pasta de entrada para a nova extensão e salvar na pasta de saída
converter_extensoes_em_pasta(pasta_entrada, pasta_saida, nova_extensao)
