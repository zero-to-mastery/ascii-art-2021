import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from community_version import handle_image_conversion

UPLOAD_FOLDER = './webapp/uploads'
TXT_FOLDER = './webapp'
KEY_FOLDER = './akey.txt'

app = Flask(__name__)
app.secret_key = "my-very-secret-key-pls"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TXT_FOLDER'] = TXT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024 # File max size set to 4MB

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def get_index():
  return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate():
  if request.method == 'POST':
    if ('file1' not in request.files) or (request.files['file1'].filename == ''):
      return 'No valid file found'

    file1 = request.files['file1']

    if file1 and allowed_file(file1.filename):
      path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file1.filename))
      file1.save(path)

      ascii_image = handle_image_conversion(path,KEY_FOLDER)
      with open('./webapp/temp.txt', 'w') as f:
        f.write(ascii_image)

      if os.path.exists(path):
        os.remove(path)
      return send_from_directory(app.config['TXT_FOLDER'], 'temp.txt', as_attachment=True)

    else:
      return 'File must be a valid jpeg, png or jpg file'


@app.route('/ztm-logo.html')
def show_ztm_logo_ascii_img():
    DEFAULT_IMAGE_PATH = './example/ztm-logo.png'
    image = handle_image_conversion(DEFAULT_IMAGE_PATH,KEY_FOLDER)
    return render_template('ztm-logo.html', image=image)


if __name__ == '__main__':
  app.run(debug=True)
