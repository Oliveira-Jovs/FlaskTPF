import os

imagens = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\BaseCompleta\images"

labels = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\BaseCompleta\labels"

print(len(os.listdir(imagens)))
print(len(os.listdir(labels)))