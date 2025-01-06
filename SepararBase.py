import os
import random
import shutil

# Caminhos das pastas
imagens_path = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\BaseCompleta\images"
labels_path = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\BaseCompleta\labels"
dataset_path = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\TPFDataSet"

# Subpastas do conjunto de dados
subdirs = ["train", "val", "test"]

# Cria as pastas principais e subpastas
for subdir in subdirs:
    os.makedirs(os.path.join(dataset_path, subdir, "images"), exist_ok=True)
    os.makedirs(os.path.join(dataset_path, subdir, "labels"), exist_ok=True)

# Listar arquivos de imagem e rótulo
imagens = os.listdir(imagens_path)
labels = os.listdir(labels_path)

# Garantir correspondência exata (baseado no nome do arquivo sem extensão)
imagens_sem_extensao = {os.path.splitext(img)[0] for img in imagens}
labels_sem_extensao = {os.path.splitext(lbl)[0] for lbl in labels}
arquivos_comuns = imagens_sem_extensao.intersection(labels_sem_extensao)

# Converter para lista para indexação
arquivos_comuns = list(arquivos_comuns)
random.shuffle(arquivos_comuns)  # Embaralhar para separar aleatoriamente

# Dividir em proporções
total = len(arquivos_comuns)
train_split = int(total * 0.7)
val_split = int(total * 0.2)

train_set = arquivos_comuns[:train_split]
val_set = arquivos_comuns[train_split:train_split + val_split]
test_set = arquivos_comuns[train_split + val_split:]


# Função para mover arquivos
def mover_arquivos(subset, subset_name):
    for arquivo in subset:
        # Mover imagens
        src_img = os.path.join(imagens_path, f"{arquivo}.jpg")  # Substituir extensão conforme necessário
        dest_img = os.path.join(dataset_path, subset_name, "images", f"{arquivo}.jpg")
        if os.path.exists(src_img):
            shutil.copy(src_img, dest_img)

        # Mover labels
        src_lbl = os.path.join(labels_path, f"{arquivo}.txt")  # Substituir extensão conforme necessário
        dest_lbl = os.path.join(dataset_path, subset_name, "labels", f"{arquivo}.txt")
        if os.path.exists(src_lbl):
            shutil.copy(src_lbl, dest_lbl)


# Mover arquivos para as pastas correspondentes
mover_arquivos(train_set, "train")
mover_arquivos(val_set, "val")
mover_arquivos(test_set, "test")

print("Separação concluída!")
