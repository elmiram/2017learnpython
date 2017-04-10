from flask import Flask
from flask import url_for, render_template, request, redirect
from pymystem3 import Mystem

m = Mystem()
app = Flask(__name__)


def add_POS(text):
    result = ''
    ana = m.analyze(text)
    for i in ana:
        result += i['text']
        if i['text'].strip() and 'analysis' in i and i['analysis']:
            pos = i['analysis'][0]['gr'].split('=')[0].split(',')[0]
            result += '<span class="pos">{}</span>'.format(pos)
    return result


@app.route('/', methods=['get', 'post'])
def index():
    if request.form:
        text = request.form['text']
        result = add_POS(text).replace('\n', '<br>')
        return render_template('index_page.html', input=text, text=result)
    return render_template('index_page.html')


if __name__ == '__main__':
    app.run(debug=True)