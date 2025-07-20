from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from model import predict_disease  # this is your custom function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)
            prediction = predict_disease(filepath)
            return render_template('index.html', prediction=prediction, image_url=filepath)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

