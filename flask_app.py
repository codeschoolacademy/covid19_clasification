from flask import Flask, request
from test_model import image_classification
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome Flask API!"

@app.route('/image', methods=['POST'])  
def main():
    if 'file' not in request.files:
        return "No file part", 400  
    
    image = request.files['file']
    
    if image.filename == '':
        return "No selected file", 400  
    
    image_data = Image.open(image.stream) 
    clasification_image = image_classification(image=image_data) 
    return clasification_image
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
