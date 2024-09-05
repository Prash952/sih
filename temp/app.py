from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model = load_model('waste_classification_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    img_file = request.files['image']
    
    if img_file:
        img = image.load_img(img_file, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize image
        
        predictions = model.predict(img_array)
        class_names = ['plastic', 'metal', 'bio-degradable', 'electrical', 'glass']  # Adjust according to your classes
        predicted_class = class_names[np.argmax(predictions)]
        
        return jsonify({'prediction': predicted_class})
    
    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True)
