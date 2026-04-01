import os
from flask import Flask, render_template, request
from services.ai_service import analyze_image
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']

        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            result = analyze_image(path)

            return render_template('result.html',
                                   image_path=path,
                                   data=result)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)