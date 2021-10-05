from flask import Flask, render_template, flash
from markupsafe import Markup

from community_version_main import get_ztm_logo_ascii_img

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ztm-logo.html')
def show_ztm_logo_ascii_img():

    image = get_ztm_logo_ascii_img()

    return render_template('ztm-logo.html', image=image)


if __name__ == '__main__':

    app.run()