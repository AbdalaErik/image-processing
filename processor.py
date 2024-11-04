from PIL import Image
import numpy as np
import os

def calculate_mean_and_std_deviation(pattern): # Função para calcular a média e o desvio padrão dos canais de uma imagem.

    pixels = np.array(pattern) # Converte a imagem para um array numpy.
    mean = np.mean(pixels, axis=(0, 1)) # Calcula a média dos valores de cada canal (R, G, B).
    std_dev = np.std(pixels, axis=(0, 1)) + 10 # Calcula o desvio padrão de cada canal, adicionando 10 para evitar valores muito baixos.

    return mean, std_dev # Retorna a média e o desvio padrão.

patterns_directory_path = 'patterns' # Define o caminho da pasta que contém as imagens padrão.

mean_and_std_deviations = [] # Lista para armazenar as médias e desvios padrão das imagens.

for file in os.listdir(patterns_directory_path): # Loop para percorrer cada arquivo no diretório de padrões.

    if file.endswith(('.png', '.jpg', '.jpeg')): # Verifica se o arquivo é uma imagem com extensão válida.

        image = Image.open(os.path.join(patterns_directory_path, file)).convert('RGB') # Abre a imagem e converte para RGB.
        mean, std_dev = calculate_mean_and_std_deviation(image) # Calcula a média e o desvio padrão da imagem.
        mean_and_std_deviations.append((mean, std_dev)) # Adiciona os resultados à lista.

# Carregar a imagem de entrada e converter para numpy array.
image = Image.open('apples.jpeg').convert('RGB') # Abre a imagem que será processada.
image_np = np.array(image) # Converte a imagem para um array numpy.

brightness_lower = 80 # Limite inferior de brilho.
brightness_upper = 220 # Limite superior de brilho.

# Calcular a luminosidade (brilho) e tolerância para cada pixel.
brightness = np.mean(image_np, axis=2) # Calcula a média dos valores de brilho por pixel.
brightness_tolerance_multiplier = np.where(
    brightness < brightness_lower, 1.5, # Se o brilho for menor que o limite inferior, aumenta a tolerância.
    np.where(brightness > brightness_upper, 0.8, 1.0) # Se o brilho for maior que o limite superior, diminui a tolerância; caso contrário, mantém.
)

for mean, std_dev in mean_and_std_deviations: # Loop para processar as médias e desvios padrão de cada padrão.

    # Define os limites inferior e superior de cor baseado na média e desvio padrão, ajustados pela tolerância de brilho.
    lower_color_bound = mean - (std_dev * brightness_tolerance_multiplier[:, :, None])
    upper_color_bound = mean + (std_dev * brightness_tolerance_multiplier[:, :, None])

    # Condições para encontrar pixels que estão dentro da faixa de cor e são predominantemente verdes.
    color_mask = (
        (image_np >= lower_color_bound) & (image_np <= upper_color_bound) # Verifica se os pixels estão dentro dos limites de cor.
    ).all(axis=2) & ((image_np[:, :, 1] > image_np[:, :, 0] + 12) & # Verifica se o canal verde é maior que os canais vermelho e azul.
                     (image_np[:, :, 1] > image_np[:, :, 2] + 12))

    image_np[color_mask] = [0, 0, 255] # Aplica a cor azul aos pixels que atendem às condições.

final_image = Image.fromarray(image_np) # Converter o array de volta para imagem.

image.show() # Exibir a imagem inicial.
final_image.show() # Exibir a imagem resultante.