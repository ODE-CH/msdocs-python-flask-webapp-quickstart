import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from utility import get_plotly_plot_wisam

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html', graphJSON=get_plotly_plot_wisam())

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name, graphJSON=get_plotly_plot_wisam())

   print('Request for hello page received with no name or blank name -- redirecting')
   return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
