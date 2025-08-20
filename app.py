from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
model = tf.keras.models.load_model("cat_dog_vit_model")

def predict_image(img_path):
    img = Image.open(img_path).resize((224,224))
    img_array = np.expand_dims(np.array(img)/255.0, axis=0)
    pred = model.predict(img_array)[0][0]
    return "Dog 🐶" if pred > 0.5 else "Cat 🐱"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            prediction = predict_image(filepath)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
