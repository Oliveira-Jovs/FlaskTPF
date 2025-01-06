import os

imagens_path = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\BaseCompleta\images"
labels_path = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\BaseCompleta\labels"

# Listar arquivos
imagens = os.listdir(imagens_path)
labels = os.listdir(labels_path)

# Obter nomes sem extensão
imagens_sem_extensao = {os.path.splitext(arquivo)[0] for arquivo in imagens}
labels_sem_extensao = {os.path.splitext(arquivo)[0] for arquivo in labels}

# Encontrar arquivos sem correspondência
imagens_nao_correspondentes = imagens_sem_extensao - labels_sem_extensao
labels_nao_correspondentes = labels_sem_extensao - imagens_sem_extensao

# Exibir resultados
if imagens_nao_correspondentes:
    print("Imagens sem correspondência:")
    for img in imagens_nao_correspondentes:
        print(img)
else:
    print("Todas as imagens têm correspondência.")

if labels_nao_correspondentes:
    print("Labels sem correspondência:")
    for lbl in labels_nao_correspondentes:
        print(lbl)
else:
    print("Todas as labels têm correspondência.")
