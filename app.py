import os
from flask import Flask, render_template, request, redirect, url_for
from model import predict_disease
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route (upload form)
@app.route('/')
def index():
    return render_template('index.html')

# Handle image upload and prediction
@app.route('/predict', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Predict disease using model.py
    result = predict_disease(filepath)

    return render_template('result.html', image_path=filepath, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)

