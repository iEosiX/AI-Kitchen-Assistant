import os
from flask import Flask, render_template, request, session, send_file
from services.ai_service import analyze_image
from services.pdf_service import generate_pdf
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkey"

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
            session['last_result'] = result

            return render_template('result.html',
                                   image_path=path,
                                   data=result)

    return render_template('index.html')

@app.route('/download')
def download():
    data = session.get('last_result')

    if not data:
        return "No data available. Please analyze an image first.", 400

    filepath = "recipe.pdf"
    generate_pdf(data, filepath)

    return send_file(filepath, 
                     as_attachment=True, 
                     download_name="AI_Kitchen_Recipe.pdf")

if __name__ == '__main__':
    app.run(debug=True)
