import os

import dotenv
from flask import Flask, render_template, request, send_from_directory, redirect, flash, url_for
from werkzeug.utils import secure_filename

from community_version import (handle_image_conversion, is_supported, save_as_img,
                               ALLOWED_EXTENSIONS)

dotenv.load_dotenv()

app = Flask(__name__)
app.config.from_pyfile('web_config.py')

config = app.config

if not os.path.exists(config['UPLOAD_FOLDER']):
    os.makedirs(config['UPLOAD_FOLDER'])


def get_ascii_keys(): #LIST COMPREHENSION?????????????????????????????????????????????
    keys = list()
    filenames = os.listdir(config['KEY_FOLDER'])
    for f in filenames:
        if f.endswith(".txt"):
            keys.append({'name': f})
            keys = sorted(keys, key=lambda k: k['name'])
    return keys


def convert_image(path, key=config['DEFAULT_KEY']):
    ascii_image = handle_image_conversion(path, os.path.join(config['KEY_FOLDER'] + key))
    with open(config['TXT_FOLDER'] + '/temp.txt', 'w') as f:
        f.write(ascii_image)
    path = config['ASCII_IMAGE_FOLDER'] + '/temp.png'
    if os.path.exists(path):
        os.remove(path)
        save_as_img(ascii_image, config['ASCII_IMAGE_FOLDER'] + '/temp.png')
    else:
        save_as_img(ascii_image, config['ASCII_IMAGE_FOLDER'] + '/temp.png')
    return ascii_image


@app.route('/')
def index():
    return render_template('index.html', **{
        'image': convert_image(config['DEFAULT_IMAGE_PATH']),
        'filename': config['DEFAULT_IMAGE_PATH'],
        'data': get_ascii_keys(),
        'key': config['DEFAULT_KEY']
        })


@app.route('/generate', methods=['POST'])
def generate():
    if ('file1' not in request.files) or not request.files['file1'].filename:
        flash('No valid file found', category='error')
        return redirect(url_for('index'))
    file1 = request.files['file1']
    if file1 and is_supported(file1.filename):
        path = os.path.join(config['UPLOAD_FOLDER'], secure_filename(file1.filename))
        file1.save(path)
        key = request.form.get('key_select')
        ascii_image = convert_image(path, key)
        if os.path.exists(path):
            os.remove(path)
        return render_template('index.html', image=ascii_image,
                               filename=file1.filename, 
                               data=get_ascii_keys(), 
                               key=key)
    else:
        flash(f"File must be one of: {', '.join(ALLOWED_EXTENSIONS)}", category='error')
        return redirect(url_for('index'))


@app.route('/download_text_file', methods=['POST'])
def download_text_file():
    return send_from_directory(config['TXT_FOLDER'], 'temp.txt', as_attachment=True)


@app.route('/download_png', methods=['POST'])
def download_png():
    return send_from_directory(config['ASCII_IMAGE_FOLDER'], 'temp.png', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
