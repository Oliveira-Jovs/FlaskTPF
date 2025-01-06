import os

# Caminho principal do dataset
dataset_path = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\TPFDataSet"

# Subpastas do dataset
subdirs = ["train", "val", "test"]

# Contador de arquivos
for subdir in subdirs:
    images_path = os.path.join(dataset_path, subdir, "images")
    labels_path = os.path.join(dataset_path, subdir, "labels")

    # Contar arquivos nas subpastas
    num_images = len(os.listdir(images_path)) if os.path.exists(images_path) else 0
    num_labels = len(os.listdir(labels_path)) if os.path.exists(labels_path) else 0

    print(f"Subdiretório: {subdir}")
    print(f"  Imagens: {num_images}")
    print(f"  Labels: {num_labels}")
    print()
