from ultralytics import YOLO

def train_model():
    model = YOLO("yolo11n.pt")
    model.train(data=r"C:\Users\oliveira\Desktop\Projetos_Pycharm\TPFtesteEngenharia\data.yaml", epochs=15)
    model.val()

if __name__ == '__main__':
    train_model()
