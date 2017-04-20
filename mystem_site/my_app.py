from flask import Flask
from flask import url_for, render_template, request, redirect
from pymystem3 import Mystem
from collections import Counter
import json
import requests


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


def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


def get_cities(group):
    users = []

    result = vk_api('groups.getMembers', group_id=group)
    members_count = result['response']['count']
    users += result['response']["users"]

    while len(users) < members_count:
        result = vk_api('groups.getMembers', group_id=group, offset=len(users))
        users += result['response']["users"]

    cities = []
    for start in range(0, len(users) + 1, 100):  # будем доставать информацию о 100 юзерах за один запрос
        user_info = vk_api('users.get', user_ids=','.join(str(i) for i in users[start:start + 100]), fields='city',
                           v='5.63')
        cities += [(c["city"]['id'], c["city"]['title']) for c in user_info['response']
                   if 'city' in c]  # эта проверка нужна, чтобы отфильтровать пользователей, удаливших страницу
    city_dict = Counter([i[1] for i in cities]).most_common()
    return city_dict


@app.route('/pos', methods=['get', 'post'])
def pos_text():
    if request.form:
        text = request.form['text']
        result = add_POS(text).replace('\n', '<br>')
        return render_template('mystem_page.html', input=text, text=result)
    return render_template('mystem_page.html')


@app.route('/cities', methods=['get', 'post'])
def cities():
    if request.form:
        group_id = request.form['group_id']
        cities = get_cities(group_id)
        return render_template('cities.html', **locals())
    return render_template('cities.html')


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)