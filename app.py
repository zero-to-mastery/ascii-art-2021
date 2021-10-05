from flask import Flask, render_template

from community_version import handle_image_conversion

DEFAULT_IMAGE_PATH = './example/ztm-logo.png'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ztm-logo.html')
def show_ztm_logo_ascii_img():
    image = handle_image_conversion(DEFAULT_IMAGE_PATH)
    return render_template('ztm-logo.html', image=image)


if __name__ == '__main__':
    app.run()
