# 🐱🐶 Cat vs Dog Classifier using Vision Transformer (ViT)

This project is a **web-based Cat vs Dog image classifier** built using **Vision Transformer (ViT)** and **Flask**, allowing users to upload an image and get predictions in real-time. The app is fully deployable on platforms like **Render.com**.

---

## **Features**

* Uses a **pretrained Vision Transformer (ViT)** for image classification.
* Classifies uploaded images as **Cat 🐱** or **Dog 🐶**.
* Simple **Flask web interface** for uploading images and viewing predictions.
* Ready for deployment on **Render.com** or other cloud platforms.

---

## **Project Structure**

```
cat_dog_app/
│
├─ app.py                 # Flask web app
├─ requirements.txt       # Python dependencies
├─ runtime.txt            # Python version (optional)
├─ cat_dog_vit_model/     # Saved TensorFlow model folder or PyTorch .pt file
├─ templates/
│   └─ index.html         # HTML template for file upload
├─ static/
│   └─ uploads/           # Folder for uploaded images
```

---

## **Setup and Installation**

1. **Clone the repository**

```bash
git clone <YOUR_REPO_URL>
cd cat_dog_app
```

2. **Create virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app locally**

```bash
python app.py
```

* Open browser at `http://127.0.0.1:5000/`
* Upload a cat or dog image to see the prediction.

---

## **Render Deployment**

1. Push the repository to GitHub.
2. Go to [Render.com](https://render.com/) → **New → Web Service**.
3. Connect your GitHub repo.
4. Configure:

   * **Environment:** Python
   * **Build Command:**

     ```bash
     pip install -r requirements.txt
     ```
   * **Start Command:**

     ```bash
     gunicorn app:app
     ```
5. Deploy and access your live app via the Render URL.

---

## **Dependencies**

* Flask
* TensorFlow
* NumPy
* Pillow
* Gunicorn
* (Optional for Hugging Face ViT: `torch`, `transformers`)

---

## **Usage**

1. Open the app in a browser.
2. Click **Choose File** and upload an image of a cat or dog.
3. Click **Predict**.
4. The app will display **Cat 🐱** or **Dog 🐶** based on the model prediction.

---

## **Notes**

* Make sure the folder `static/uploads/` exists, otherwise uploaded files cannot be saved.
* Ensure `cat_dog_vit_model/` is included in the repo for the model to load correctly.
* Python 3.10 is recommended for compatibility with TensorFlow Addons and ViT packages.

---

## **Author**

**Sangram Magar**
 M.Tech in AI | AI Enthusiast
