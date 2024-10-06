from ultralytics import YOLO
def get_model(model_path: str):
    model = YOLO(model_path)
    return model

def image_train(model_path: str, dataset, epochs: int, image_size: int):
    model = YOLO(model_path)
    results = model.train(
        dataset=dataset,
        epochs = epochs,
        imgsz = image_size
    )
    return results