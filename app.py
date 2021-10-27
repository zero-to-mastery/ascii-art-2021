import os
import pathlib

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import redirect, secure_filename

from community_version import handle_image_conversion, is_supported, ALLOWED_EXTENSIONS, save_as_img

UPLOAD_FOLDER = './webapp/uploads'
TXT_FOLDER = './webapp'
KEY_FOLDER = './akey.txt'
ASCII_IMAGE_FOLDER = './webapp'
DEFAULT_IMAGE_PATH = './example/ztm-logo.png'
pathlib.Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.secret_key = "my-very-secret-key-pls"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TXT_FOLDER'] = TXT_FOLDER
app.config['ASCII_IMAGE_FOLDER'] = ASCII_IMAGE_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024  # File max size set to 4MB

def convert_image(path):
    ascii_image = handle_image_conversion(path, KEY_FOLDER)
    with open(app.config['TXT_FOLDER'] + '/temp.txt', 'w') as f:
        f.write(ascii_image)
    save_as_img(ascii_image, app.config['ASCII_IMAGE_FOLDER'] + '/temp.png')
    return ascii_image

@app.route('/')
def get_index():
    #text_image = handle_image_conversion(DEFAULT_IMAGE_PATH, KEY_FOLDER)
    return render_template('index.html', image = convert_image(DEFAULT_IMAGE_PATH), filename = DEFAULT_IMAGE_PATH)


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        if ('file1' not in request.files) or (request.files['file1'].filename == ''):
            return 'No valid file found' #?Put this as an error message on main page.

        file1 = request.files['file1']

        if file1 and is_supported(file1.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file1.filename))
            file1.save(path)

            ascii_image = convert_image(path)

            if os.path.exists(path):
                os.remove(path)

            return render_template('index.html', image = ascii_image, filename = file1.filename)

        else:
            return f"File must be one of: {', '.join(ALLOWED_EXTENSIONS)}"


@app.route('/download_text_file', methods=['GET', 'POST'])
def download_text_file():
    if request.method == 'POST':
        return send_from_directory(app.config['TXT_FOLDER'], 'temp.txt', as_attachment=True)


@app.route('/download_png', methods=['GET', 'POST'])
def download_png():
    if request.method == 'POST':
        return send_from_directory(app.config['ASCII_IMAGE_FOLDER'], 'temp.png', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
