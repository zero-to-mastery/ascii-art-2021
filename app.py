import os

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from community_version import handle_image_conversion, is_supported, ALLOWED_EXTENSIONS, save_as_img

UPLOAD_FOLDER = './webapp/uploads'
TXT_FOLDER = './webapp'
KEY_FOLDER = './akey.txt'
DEFAULT_IMAGE_PATH = './example/ztm-logo.png'

app = Flask(__name__)
app.secret_key = "my-very-secret-key-pls"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TXT_FOLDER'] = TXT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024  # File max size set to 4MB


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        if ('file1' not in request.files) or (request.files['file1'].filename == ''):
            return 'No valid file found'

        file1 = request.files['file1']

        if file1 and is_supported(file1.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file1.filename))
            file1.save(path)

            ascii_image = handle_image_conversion(path, KEY_FOLDER)
            with open('./webapp/temp.txt', 'w') as f:
                f.write(ascii_image)

            if os.path.exists(path):
                os.remove(path)
            return send_from_directory(app.config['TXT_FOLDER'], 'temp.txt', as_attachment=True)

        else:
            return f"File must be one of: {', '.join(ALLOWED_EXTENSIONS)}"


@app.route('/ztm-logo.html', methods=['GET', 'POST'])
def show_ztm_logo_ascii_img():
    text_image = handle_image_conversion(DEFAULT_IMAGE_PATH, KEY_FOLDER)
    #form request
    if request.method == 'POST':
        image = save_as_img(text_image, 'ztm-logo-ascii.png')

    return render_template('ztm-logo.html', image=text_image)


if __name__ == '__main__':
    app.run(debug=True)
