import cv2
import os

imagens_path = r'/SegmentacaoTPFTestYolo/BaseDadosTaludeNaoGrama/Joao'
rotulos_path = r'/SegmentacaoTPFTestYolo/BaseDadosTaludeNaoGrama/labels'
saida_path = r'/SegmentacaoTPFTestYolo/BaseDadosTaludeNaoGrama/saida_com_bboxes'  # Pasta de saída

# Cria a pasta de saída, caso não exista
if not os.path.exists(saida_path):
    os.makedirs(saida_path)

# Lista as imagens e rótulos
imagens = [f for f in os.listdir(imagens_path) if f.endswith(('.jpg', '.png'))]
imagens.sort()  # Ordena as imagens para exibir em ordem

# Função para desenhar as bounding boxes com as classes
def desenhar_bounding_boxes(imagem_path, rotulo_path):
    # Carregar a imagem
    img = cv2.imread(imagem_path)

    # Ler os rótulos
    with open(rotulo_path, 'r') as file:
        linhas = file.readlines()

    # Para cada linha de rótulo (uma caixa delimitadora)
    for linha in linhas:
        valores = linha.strip().split()

        # Assumindo que o formato é: classe centro_x centro_y largura altura
        classe, cx, cy, w, h = map(float, valores)

        # Convertendo para as coordenadas reais (em pixels)
        h_img, w_img = img.shape[:2]
        x1 = int((cx - w / 2) * w_img)
        y1 = int((cy - h / 2) * h_img)
        x2 = int((cx + w / 2) * w_img)
        y2 = int((cy + h / 2) * h_img)

        # Definindo o nome da classe
        if int(classe) == 0:
            nome_classe = 'Talude'
            cor = (0, 255, 0)  # Cor verde para Talude
        else:
            nome_classe = 'Sem Grama'
            cor = (0, 0, 255)  # Cor vermelha para Sem Grama

        # Desenhar a caixa com a classe
        cv2.rectangle(img, (x1, y1), (x2, y2), cor, 2)

        # Adicionar o texto da classe
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, nome_classe, (x1, y1 - 10), font, 0.9, cor, 2)

    return img


# Processar e salvar as imagens
for imagem_nome in imagens:
    imagem_path = os.path.join(imagens_path, imagem_nome)
    rotulo_path = os.path.join(rotulos_path, imagem_nome.replace('.jpg', '.txt').replace('.png', '.txt'))

    if os.path.exists(rotulo_path):
        imagem_com_bboxes = desenhar_bounding_boxes(imagem_path, rotulo_path)

        # Salvar a imagem com as bounding boxes
        imagem_saida_path = os.path.join(saida_path, imagem_nome)
        cv2.imwrite(imagem_saida_path, imagem_com_bboxes)

print("Processamento concluído! As imagens com as bounding boxes foram salvas.")
