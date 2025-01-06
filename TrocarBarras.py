caminhoBase = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\TPFDataSet"

caminhoTrain = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\TPFDataSet\train\images"

caminhoVal = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\TPFDataSet\val\images"

caminhoTest = r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\TPFDataSet\test\images"

caminho_corrigidoBase = caminhoBase.replace("\\", "/")
caminho_corrigidoTrain = caminhoTrain.replace("\\", "/")
caminho_corrigidoVal= caminhoVal.replace("\\", "/")
caminho_corrigidoTest = caminhoTest.replace("\\", "/")

print(caminho_corrigidoBase)
print(caminho_corrigidoTrain)
print(caminho_corrigidoVal)
print(caminho_corrigidoTest)
