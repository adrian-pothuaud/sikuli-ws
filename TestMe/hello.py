from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

if __name__ == '__main__':
    app.run()
